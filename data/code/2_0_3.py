def calculate_total_volume(filepath):
    total_volume = 0.0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    volume_str = line.strip()
                    if volume_str:
                        volume = float(volume_str)
                        total_volume += volume
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except IOError:
        print(f"Error: Could not read file at {filepath}")
        return None
    return total_volume
if __name__ == '__main__':
    sample_filename = "volume_data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10.5\n")
            f.write("22.3\n")
            f.write("5.0\n")
            f.write("invalid_data\n")
            f.write("1.25\n")
        total = calculate_total_volume(sample_filename)
        if total is not None:
            print(f"Total volume calculated: {total}")
    except Exception as e:
        print(f"An unexpected error occurred during setup or execution: {e}")