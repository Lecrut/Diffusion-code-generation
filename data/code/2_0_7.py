import os
def calculate_total_volume(filepath):
    total_volume = 0.0
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    volume = float(line.strip())
                    total_volume += volume
                except ValueError:
                    continue
        return total_volume
    except FileNotFoundError:
        return None
    except IOError:
        return None
if __name__ == '__main__':
    sample_filename = "volume_data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10.5\n")
            f.write("22.3\n")
            f.write("5.0\n")
            f.write("invalid_data\n")
            f.write("1.25\n")
        result = calculate_total_volume(sample_filename)
        if result is not None:
            print(f"Total volume calculated: {result}")
        else:
            print("Error: Could not read or process the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if os.path.exists(sample_filename):
            os.remove(sample_filename)