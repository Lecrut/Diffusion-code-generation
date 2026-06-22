import argparse
import re
import sys
import io

def convert_temps_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    
    def replace_celsius(match):
        temp_c = float(match.group(1))
        temp_f = (temp_c * 9/5) + 32
        return f"{temp_f:.2f}F"
    
    pattern = r'(-?\d+\.?\d*)\s*C'
    result = re.sub(pattern, replace_celsius, content)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Celsius temperatures to Fahrenheit in a file.')
    parser.add_argument('file_path', type=str, help='Path to the input file')
    
    import sys
    sys.argv = ['script', 'temp_data.txt']
    
    args = parser.parse_args()
    
    sample_content = "The temperature today is 25C. Tomorrow it might reach 30C or drop to 15C. At night it will be -5C."
    
    with open('temp_data.txt', 'w') as f:
        f.write(sample_content)
    
    output = convert_temps_in_file(args.file_path)
    print(output)