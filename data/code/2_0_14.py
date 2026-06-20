import os

def calculate_total_volume(file_path: str) -> float:
    if not os.path.exists(file_path):
        return 0.0
    with open(file_path, 'r') as f:
        content = f.read()
    lines = content.strip().splitlines()
    total = 0.0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            value = float(line)
            total += value
        except ValueError:
            continue
    return total

if __name__ == '__main__':
    sample_file = '/tmp/volume_data.txt'
    with open(sample_file, 'w') as f:
        f.write("10.5\n")
        f.write("20.0\n")
        f.write("30.5\n")
        f.write("invalid\n")
        f.write("\n")
    total_volume = calculate_total_volume(sample_file)
    print(total_volume)
    os.remove(sample_file)