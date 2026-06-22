def calculate_total_volume(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    volume = float(line.strip())
                    total_volume += volume
                except ValueError:
                    print(f"Skipping invalid volume value: {line.strip()}")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except IOError:
        print("Error: An I/O error occurred while reading the file.")
    return total_volume

if __name__ == '__main__':
    sample_file_content = """10.5
20.3
invalid_value
30.7"""
    with open('sample_volumes.txt', 'w') as f:
        f.write(sample_file_content)
    
    total_volume = calculate_total_volume('sample_volumes.txt')
    print(f"Total Volume: {total_volume}")