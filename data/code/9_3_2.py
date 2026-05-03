def convert_volume(volume_liters):
    volume_cubic_meters = volume_liters / 1000.0
    return volume_liters, volume_cubic_meters
def process_volume_file(filename):
    volume_data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    volume_liters = float(line.strip())
                    volume_data.append(volume_liters)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        return
    print("\nVolume Conversions:")
    for volume_liters in volume_data:
        liters, cubic_meters = convert_volume(volume_liters)
        print(f"Liters: {liters:.2f}, Cubic Meters: {cubic_meters:.4f}")
if __name__ == '__main__':
    sample_filename = "volumes.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("1500.5\n")
            f.write("2500\n")
            f.write("abc\n")
            f.write("3000.75\n")
            f.write("1000\n")
    except IOError:
        print("Error: Could not create sample file.")
        exit()
    process_volume_file(sample_filename)