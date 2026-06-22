import os
import tempfile

def process_volume_measurements(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return [{"error": "File not found"}]
    except IOError:
        return [{"error": "IO error reading file"}]

    results = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            volume_liters = float(line)
            volume_cubic_meters = volume_liters / 1000.0
            results.append({
                "liters": volume_liters,
                "cubic_meters": volume_cubic_meters
            })
        except ValueError:
            results.append({
                "error": f"Invalid value: {line}"
            })
    return results

if __name__ == '__main__':
    sample_data = "1.5\n100.0\n-5.0\nabc\n5000.0"
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(sample_data)
        temp_path = f.name

    try:
        results = process_volume_measurements(temp_path)
        print(results)
    finally:
        os.unlink(temp_path)