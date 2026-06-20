import csv
from io import StringIO

def calculate_total_volume(volume_data_string):
    total_volume = 0.0
    lines = volume_data_string.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            volume_value = float(line)
            if volume_value < 0:
                raise ValueError("Volume cannot be negative")
            total_volume += volume_value
        except ValueError:
            continue
    return total_volume

def calculate_total_volume_from_file(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    volume_value = float(line)
                    if volume_value < 0:
                        raise ValueError("Volume cannot be negative")
                    total_volume += volume_value
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    except IOError:
        return None
    return total_volume

if __name__ == '__main__':
    sample_data = """10.5
20.3
-5.0
abc
15.2
"""
    total = calculate_total_volume(sample_data)
    print(total)

    temp_file = "sample_volumes.txt"
    with open(temp_file, 'w') as f:
        f.write("10.5\n20.3\n15.2\n")
    file_total = calculate_total_volume_from_file(temp_file)
    print(file_total)

    non_existent_total = calculate_total_volume_from_file("non_existent_file.txt")
    print(non_existent_total)