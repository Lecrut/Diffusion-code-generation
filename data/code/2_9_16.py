import os

def calculate_total_volume_from_file(file_path):
    total_volume = 0.0
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("10.5\n20.3\n15.0\ninvalid\n30.2\n")
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        try:
            value = float(cleaned_line)
            total_volume += value
        except ValueError:
            continue
    
    return total_volume

if __name__ == '__main__':
    sample_file = "volumes.txt"
    result = calculate_total_volume_from_file(sample_file)
    print(result)