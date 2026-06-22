import tempfile
import os

def calculate_total_volume_from_file(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                try:
                    volume = float(stripped_line)
                    total_volume += volume
                except ValueError:
                    continue
    except FileNotFoundError:
        raise
    except IOError:
        raise
    return total_volume

def run_sample():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        tmp.write("10.5\n")
        tmp.write("20.3\n")
        tmp.write("invalid\n")
        tmp.write("5.2\n")
        tmp_file = tmp.name

    try:
        result = calculate_total_volume_from_file(tmp_file)
        return result
    finally:
        os.unlink(tmp_file)

if __name__ == '__main__':
    print(run_sample())