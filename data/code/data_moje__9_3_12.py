import os
import tempfile

def convert_volume(volume_ml):
    liters = volume_ml / 1000.0
    cubic_meters = volume_ml / 1000000.0
    return liters, cubic_meters

def process_volume_file(filepath):
    results = []
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filepath} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            volume_ml = float(line)
            liters, cubic_meters = convert_volume(volume_ml)
            results.append((volume_ml, liters, cubic_meters))
        except ValueError:
            continue

    return results

def main():
    sample_values = ["1000", "500", "2000", "invalid", "3.5"]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp_path = tmp.name
        for val in sample_values:
            tmp.write(f"{val}\n")

    try:
        results = process_volume_file(tmp_path)
        for volume_ml, liters, cubic_meters in results:
            print(f"{volume_ml} ml = {liters} liters = {cubic_meters} cubic meters")
    except Exception as e:
        print(e)
    finally:
        os.unlink(tmp_path)

if __name__ == '__main__':
    main()