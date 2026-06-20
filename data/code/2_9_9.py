import tempfile
import os

def parse_volume_lines(text_content):
    accumulated_volume = 0.0
    parsed_count = 0
    error_count = 0
    lines = text_content.splitlines()
    for raw_line in lines:
        clean_line = raw_line.strip()
        if not clean_line:
            continue
        try:
            numeric_value = float(clean_line)
            accumulated_volume += numeric_value
            parsed_count += 1
        except ValueError:
            error_count += 1
    return accumulated_volume, parsed_count, error_count

def sum_volumes_from_file(filepath):
    try:
        with open(filepath, 'r') as file_handle:
            content = file_handle.read()
        total, count, errors = parse_volume_lines(content)
        return total
    except FileNotFoundError:
        raise
    except IOError:
        raise

if __name__ == '__main__':
    sample_content = "10.5\n20.0\ninvalid_entry\n30.25\n-5.0\n\nhello\n45.5"
    temporary_file_descriptor, temporary_path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(temporary_file_descriptor, 'w') as temp_file:
            temp_file.write(sample_content)
        
        computed_total = sum_volumes_from_file(temporary_path)
        print(computed_total)
    finally:
        os.unlink(temporary_path)