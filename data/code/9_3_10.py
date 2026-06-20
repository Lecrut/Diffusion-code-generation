import os
import tempfile

def read_and_convert_volumes(file_path):
    results = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    volume_value = float(line)
                    liters = volume_value
                    cubic_meters = volume_value / 1000.0
                    results.append((volume_value, liters, cubic_meters))
                except ValueError:
                    continue
    except FileNotFoundError:
        raise FileNotFoundError(f'The file {file_path} was not found.')
    except PermissionError:
        raise PermissionError(f'Permission denied to read the file {file_path}.')
    except IOError as e:
        raise IOError(f'An error occurred while reading the file {file_path}: {e}')
    return results
if __name__ == '__main__':
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as tmp_file:
        tmp_file.write('100\n')
        tmp_file.write('250.5\n')
        tmp_file.write('1000\n')
        tmp_file_path = tmp_file.name
    try:
        results = read_and_convert_volumes(tmp_file_path)
        for original, liters, cubic_meters in results:
            print(f'Original: {original}, Liters: {liters}, Cubic Meters: {cubic_meters}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        os.remove(tmp_file_path)