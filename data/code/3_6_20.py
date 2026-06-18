import argparse
from pathlib import Path

def celsius_to_fahrenheit(c: float) -> str:
    """Convert a temperature in Celsius to Fahrenheit."""
    return f"{(c * 9 / 5 + 32):.1f}°F"

def process_file(file_path: str) -> None:
    """Read the file, convert temperatures, and write back to disk."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple heuristic: replace occurrences of "X°C" or "X C" where X is a number
        import re
        
        def replacer(match):
            temp_str = match.group(1)
            try:
                celsius_value = float(temp_str)
                return celsius_to_fahrenheit(celsius_value)
            except ValueError:
                # If not a valid number, keep original string unchanged to avoid breaking the file structure too much
                return match.group(0).replace("°C", "").strip()

        pattern = r'(\d+\.?\d*)\s*°?C'
        
        new_content = re.sub(pattern, replacer, content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read/write file '{file_path}'.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert temperature values in a text file from Celsius to Fahrenheit.")
    
    # Note: Using optional argument (-i) instead of required (--input) as per constraint "no argparse required arguments" and "never call input()".
    parser.add_argument('-i', '--input-file', type=str, help='Path to the input file containing temperatures.')

    args = parser.parse_args()

    # Hard-coded sample values for demonstration since no user input or files are allowed at runtime.
    if not args.input_file:
        print("This script expects a file path as an argument (e.g., python script.py -i data.txt).")
        print("Since this is the default execution without arguments, here is a simulated dry-run output:")

        # Simulating content processing on hypothetical sample values provided in code logic conceptually:
        samples = [25.0, 10.5, -4]
        
        for temp_c in samples:
            print(f"Original (C): {temp_c}°C")
            result_f = celsius_to_fahrenheit(temp_c)
            print(f"Converted (F): {result_f}")

    else:
        process_file(args.input_file)