def read_and_calculate_total_volume(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                value = float(line)
                total_volume += value
            except ValueError:
                continue
    except FileNotFoundError:
        return 0.0
    except IOError:
        return 0.0
    return total_volume

if __name__ == '__main__':
    import os
    import tempfile

    sample_data = ["10.5", "20.0", "5.5", "invalid", "3.0"]
    temp_file_path = "temp_volumes.txt"
    
    with open(temp_file_path, "w") as f:
        for item in sample_data:
            f.write(item + "\n")
    
    result = read_and_calculate_total_volume(temp_file_path)
    print(result)
    
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)