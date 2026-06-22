import os

def convert_volume_measurements(input_path):
    if not os.path.exists(input_path):
        return []
    
    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()
    except IOError:
        return []

    results = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        try:
            val_liters = float(stripped)
            val_cubic_m = val_liters / 1000.0
            results.append((val_liters, val_cubic_m))
        except ValueError:
            continue
    return results

if __name__ == '__main__':
    sample_data = [1000.0, 500.5, 25.75, 0.1]
    sample_filename = 'volume_data.txt'
    
    with open(sample_filename, 'w') as f:
        for val in sample_data:
            f.write(f"{val}\n")
            
    conversions = convert_volume_measurements(sample_filename)
    
    for liters, cubic_meters in conversions:
        print(f"Liters: {liters}, Cubic Meters: {cubic_meters}")
    
    os.remove(sample_filename)