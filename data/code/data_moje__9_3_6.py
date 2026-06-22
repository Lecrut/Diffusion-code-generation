import os
import tempfile

def convert_volumes(measurements, unit="liters"):
    results = []
    for measurement in measurements:
        if unit.lower() == "liters":
            cubic_meters = measurement / 1000.0
            liters = measurement
        elif unit.lower() == "cubic_meters":
            cubic_meters = measurement
            liters = measurement * 1000.0
        else:
            raise ValueError("Unsupported unit")
        results.append((liters, cubic_meters))
    return results

def process_volume_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return []
    except IOError:
        return []

    measurements = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        try:
            value = float(stripped)
            measurements.append(value)
        except ValueError:
            continue

    return convert_volumes(measurements, "liters")

if __name__ == '__main__':
    sample_data = "500\n1500\n750.5\n-100\n"

    tmp = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
    try:
        tmp.write(sample_data)
        tmp.flush()
        result = process_volume_file(tmp.name)
        print(result)
    finally:
        os.unlink(tmp.name)