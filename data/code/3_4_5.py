import argparse
import sys
import os

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

def process_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        content = f.read()
    
    parts = content.split()
    converted_parts = []
    
    for part in parts:
        clean_part = part.replace(',', '')
        if 'C' in clean_part or 'c' in clean_part:
            try:
                val_str = clean_part.replace('C', '').replace('c', '')
                val = float(val_str)
                converted_val = celsius_to_fahrenheit(val)
                converted_str = f"{converted_val:.2f} F"
                if ',' in part:
                    converted_str += ','
                converted_parts.append(converted_str)
            except ValueError:
                converted_parts.append(part)
        else:
            converted_parts.append(part)
            
    return ' '.join(converted_parts)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert temperatures in a file from C to F")
    parser.add_argument('file_path', type=str, help="Path to the file")
    
    args = parser.parse_args()
    
    if os.path.exists(args.file_path):
        result = process_file(args.file_path)
        print(result)
    else:
        print(f"Error: File {args.file_path} not found.")