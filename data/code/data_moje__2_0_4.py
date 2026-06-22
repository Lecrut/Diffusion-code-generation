import os
import tempfile

def calculate_total_volume_from_file(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    volume = float(line)
                    total_volume += volume
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    except IOError:
        return None
    return total_volume

if __name__ == '__main__':
    test_data = "10.5\n20.3\n-5.0\ninvalid\n30.0"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp:
        tmp.write(test_data)
        temp_path = tmp.name

    result = calculate_total_volume_from_file(temp_path)
    print(result)

    os.unlink(temp_path)