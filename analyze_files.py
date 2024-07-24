import os
import re

def find_info_types(text):
    # Regular expressions for different types of information
    patterns = {
        'SSN': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
        'Email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
        'Phone': re.compile(r'\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'),
        'Credit Card': re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b')
    }

    found_info = {key: [] for key in patterns}

    for info_type, pattern in patterns.items():
        matches = pattern.findall(text)
        if matches:
            found_info[info_type] = matches

    return found_info

def process_files(source_dir):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                
                found_info = find_info_types(content)
                
                found_info_str = ', '.join(f'{info_type}: {", ".join(matches)}' for info_type, matches in found_info.items() if matches)
                
                if found_info_str:
                    print(f"File '{filename}' contains: {found_info_str}")
                else:
                    print(f"File '{filename}' does not contain any recognized information types")

# Example usage
source_directory = 'C:/Users/amuttaki/Pictures/Filesi'

process_files(source_directory)