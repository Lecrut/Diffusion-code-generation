import argparse
import re
import sys
import os

def convert_celsius_to_fahrenheit(value):
    return (value * 9 / 5) + 32

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Error: File '{file_path}' not found.\n")
        return None
    except PermissionError:
        sys.stderr.write(f"Error: Permission denied reading '{file_path}'.\n")
        return None

    def replace_temp(match):
        number_str = match.group(1)
        try:
            number = float(number_str)
            converted = convert_celsius_to_fahrenheit(number)
            if converted == int(converted):
                return f"{int(converted)}°F"
            return f"{converted:.2f}°F"
        except ValueError:
            return match.group(0)

    pattern = r'(-?\d+(?:\.\d+)?)\s*°C'
    new_content = re.sub(pattern, replace_temp, content)
    return new_content

def run_conversion(file_path):
    result = process_file(file_path)
    if result is not None:
        return result
    return "Conversion failed."

if __name__ == '__main__':
    import tempfile

    sample_content = """
    Weather Report for Today
    Morning: 20°C
    Afternoon: 25°C
    Evening: 15°C
    Night: 10°C
    Extreme: -5°C
    """

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as tmp_file:
        tmp_file.write(sample_content)
        temp_file_path = tmp_file.name

    try:
        output = run_conversion(temp_file_path)
        print(output)
    finally:
        os.unlink(temp_file_path)