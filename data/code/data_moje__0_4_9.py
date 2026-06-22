import tempfile
import os

CONVERSION_FACTOR = 1.09361

def parse_meters_from_lines(lines):
    valid_lengths = []
    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        try:
            value = float(stripped)
            valid_lengths.append(value)
        except ValueError:
            valid_lengths.append(0.0)
    return valid_lengths

def convert_meters_to_yards(lengths):
    return [m * CONVERSION_FACTOR for m in lengths]

def simulate_file_read(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return parse_meters_from_lines(lines)

if __name__ == '__main__':
    test_values = [1.5, 5.25, 100.0, 0.1]
    fd, temp_path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(fd, 'w') as temp_file:
            for val in test_values:
                temp_file.write(f"{val}\n")
        
        input_lengths = simulate_file_read(temp_path)
        output_lengths = convert_meters_to_yards(input_lengths)
        
        for orig, conv in zip(input_lengths, output_lengths):
            print(f"{orig} meters is {conv} yards")
    finally:
        os.unlink(temp_path)