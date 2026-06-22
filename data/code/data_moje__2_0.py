import os
import tempfile

def calculate_total_volume(file_path):
    total = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    volume = float(stripped)
                    total += volume
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    except IOError:
        return None
    return total

if __name__ == '__main__':
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
    temp_path = temp_file.name
    try:
        temp_file.write("10.5\n")
        temp_file.write("20.3\n")
        temp_file.write("invalid\n")
        temp_file.write("5.2\n")
        temp_file.close()
        result = calculate_total_volume(temp_path)
        print(result)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)