import os
import tempfile

def convert_volume(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return [("Error", "File not found")]
    except IOError:
        return [("Error", "Could not read file")]

    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            value = float(line)
        except ValueError:
            results.append((line, "Invalid number"))
            continue

        liters = value * 1000
        cubic_meters = value
        results.append((f"{value} m^3", f"{liters} L, {cubic_meters} m^3"))

    return results

def main():
    sample_data = "1.5\n2.3\n0.001\nabc\n-5.0"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(sample_data)
        temp_path = f.name

    try:
        results = convert_volume(temp_path)
        for original, converted in results:
            print(f"{original} -> {converted}")
    finally:
        os.unlink(temp_path)

if __name__ == '__main__':
    main()