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
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return
    except IOError as e:
        print(f"Error reading file: {e}")
        return
    print("Volume Conversions:")
    for volume_liters in volume_data:
        liters, cubic_meters = convert_volume(volume_liters)
        print(f"Liters: {liters:.2f}, Cubic Meters: {cubic_meters:.4f}")
if __name__ == '__main__':
    sample_filename = "volumes.txt"
    sample_data = [
        "1500.5",
        "2500",
        "500.75",
        "invalid_data",
        "3000"
    ]
    try:
        with open(sample_filename, 'w') as f:
            for data in sample_data:
                f.write(data + "\n")
        process_volume_file(sample_filename)
    except IOError as e:
        print(f"An error occurred during file setup: {e}")