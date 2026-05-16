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
    sample_data = [
        "10.5",
        "22.1",
        "5.0",
        "invalid_data",
        "15.8"
    ]
    try:
        with open(sample_filename, 'w') as f:
            for data in sample_data:
                f.write(data + "\n")
        result = calculate_total_volume(sample_filename)
        if result is not None:
            print(f"Total volume calculated: {result}")
    except IOError as e:
        print(f"An error occurred during file setup: {e}")
    finally:
        if os.path.exists(sample_filename):
            os.remove(sample_filename)