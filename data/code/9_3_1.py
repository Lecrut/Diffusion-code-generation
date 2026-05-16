import os
def convert_volume(volume_liters):
    volume_cubic_meters = volume_liters / 1000.0
    return volume_liters, volume_cubic_meters
def process_volume_file(filepath):
    volume_data = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    volume_liters = float(line.strip())
                    volume_data.append(volume_liters)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
        return volume_data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
if __name__ == '__main__':
    sample_filename = "volumes.txt"
    sample_data = [
        "1500.5",
        "2500",
        "1000",
        "invalid_data",
        "3000.75"
    ]
    try:
        with open(sample_filename, 'w') as f:
            for item in sample_data:
                f.write(item + "\n")
    except IOError as e:
        print(f"Could not write sample file: {e}")
        exit()
    volumes_in_liters = process_volume_file(sample_filename)
    if volumes_in_liters is not None:
        print("Volume Conversions:")
        for volume_liters in volumes_in_liters:
            liters, cubic_meters = convert_volume(volume_liters)
            print(f"Liters: {liters:.2f}, Cubic Meters: {cubic_meters:.4f}")