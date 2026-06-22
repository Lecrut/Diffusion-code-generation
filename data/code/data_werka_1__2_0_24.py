def calculate_total_volume(file_path):
    try:
        with open(file_path, 'r') as file:
            total_volume = 0.0
            for line in file:
                try:
                    volume = float(line.strip())
                    total_volume += volume
                except ValueError:
                    print(f"Skipping invalid volume value: {line.strip()}")
        return total_volume
    except FileNotFoundError:
        print("File not found.")
        return None
    except IOError:
        print("Error reading file.")
        return None

if __name__ == '__main__':
    sample_file_path = 'volumes.txt'
    with open(sample_file_path, 'w') as f:
        f.write("10.5\n20.3\ninvalid\n30.7\n")

    total_volume = calculate_total_volume(sample_file_path)
    if total_volume is not None:
        print(f"Total Volume: {total_volume}")