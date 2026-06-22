def calculate_total_volume(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
            return sum(volumes)
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except ValueError:
        print("Error: The file contains invalid volume values.")
        return None

if __name__ == '__main__':
    sample_file_path = 'sample_volumes.txt'
    total_volume = calculate_total_volume(sample_file_path)
    if total_volume is not None:
        print(f"Total Volume: {total_volume}")