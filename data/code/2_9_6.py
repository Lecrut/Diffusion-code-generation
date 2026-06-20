import os
import tempfile

def calculate_total_volume(file_path):
    total_volume = 0.0
    errors = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line_num, line in enumerate(lines, start=1):
        stripped_line = line.strip()
        if not stripped_line:
            continue
        try:
            value = float(stripped_line)
            total_volume += value
        except ValueError:
            errors.append(line_num)
    
    return total_volume, errors

def main():
    content = "10.5\n20.0\ninvalid\n30.5\n"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_file.write(content)
        temp_path = temp_file.name
    
    try:
        total, errors = calculate_total_volume(temp_path)
        print(total)
        print(errors)
    finally:
        os.unlink(temp_path)

if __name__ == '__main__':
    main()