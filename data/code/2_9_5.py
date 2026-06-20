import os
import tempfile

def calculate_total_volume(volume_strings):
    total = 0.0
    for s in volume_strings:
        try:
            total += float(s)
        except (ValueError, TypeError):
            continue
    return total

def read_volumes_from_file(filepath):
    volumes = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                volumes.append(line)
    return volumes

def main():
    sample_lines = ["1.5", "2.3", "invalid", "0.2", "", "3"]
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        for line in sample_lines:
            tmp.write(line + '\n')
        tmp_path = tmp.name

    try:
        volumes = read_volumes_from_file(tmp_path)
        result = calculate_total_volume(volumes)
        print(result)
    finally:
        os.unlink(tmp_path)

if __name__ == '__main__':
    main()