import os

def convert_volumes(volume_list):
    results = []
    for vol in volume_list:
        liters = vol * 3.78541
        cubic_meters = liters / 1000.0
        results.append((liters, cubic_meters))
    return results

def process_volumes_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return []
    except IOError:
        return []

    volumes = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        try:
            val = float(stripped)
            volumes.append(val)
        except ValueError:
            continue

    return convert_volumes(volumes)

if __name__ == '__main__':
    sample_data = [1.0, 2.5, 10.0]
    results = process_volumes_from_file("nonexistent_file.txt")
    if not results:
        results = convert_volumes(sample_data)
    for liters, cubic_meters in results:
        print(f"Liters: {liters}, Cubic Meters: {cubic_meters}")