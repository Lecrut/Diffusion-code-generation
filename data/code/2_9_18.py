import os
import tempfile

def parse_volumes_from_file(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    value = float(stripped)
                    total_volume += value
                except ValueError:
                    continue
    except FileNotFoundError:
        raise
    except IOError:
        return 0.0
    return total_volume

def create_temp_volume_file(content):
    fd, path = tempfile.mkstemp(suffix='.txt', prefix='volume_')
    with os.fdopen(fd, 'w') as f:
        f.write(content)
    return path

if __name__ == '__main__':
    sample_data = "10.5\n20.0\nbad_value\n30.25\n-5.0"
    temp_file_path = create_temp_volume_file(sample_data)
    try:
        result = parse_volumes_from_file(temp_file_path)
        print(result)
    finally:
        os.unlink(temp_file_path)