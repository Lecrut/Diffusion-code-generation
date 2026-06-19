def calculate_total_volume(file_path):
    try:
        with open(file_path, 'r') as file:
            volumes = file.readlines()
            total_volume = sum(float(volume.strip()) for volume in volumes if volume.strip().replace('.', '', 1).isdigit())
            return total_volume
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except ValueError:
        print("Error: The file contains non-numeric data.")
        return None

if __name__ == '__main__':
    sample_file_path = 'volumes.txt'
    with open(sample_file_path, 'w') as sample_file:
        sample_file.write("10.5\n20.3\n30.7\n")

    total_volume = calculate_total_volume(sample_file_path)
    if total_volume is not None:
        print(f"Total Volume: {total_volume}")