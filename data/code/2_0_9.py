import os
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
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
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
            f.write("30.1\n")
        result = calculate_total_volume(sample_filename)
        if result is not None:
            print(f"Total volume calculated: {result}")
    except IOError as e:
        print(f"An error occurred during file setup or execution: {e}")