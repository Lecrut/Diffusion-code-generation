import os
import tempfile

def convert_volumes_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            value = float(line)
        except ValueError:
            continue
        liters = value * 0.001
        cubic_meters = value * 0.000001
        results.append((value, liters, cubic_meters))

    return results

def main():
    sample_data = [
        "1000",
        "500",
        "250.5",
        "0",
        "-100"
    ]

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        for item in sample_data:
            f.write(f"{item}\n")
        temp_path = f.name

    try:
        results = convert_volumes_from_file(temp_path)
        for original, liters, cubic_meters in results:
            print(f"Original: {original}, Liters: {liters}, Cubic Meters: {cubic_meters}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    main()