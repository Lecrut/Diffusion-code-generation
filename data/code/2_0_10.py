import os

def calculate_total_volume(file_path: str) -> float:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    total_volume = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                volume = float(line)
                total_volume += volume
            except ValueError:
                continue
    return total_volume

def create_sample_file(file_path: str) -> None:
    with open(file_path, 'w') as f:
        f.write("10.5\n")
        f.write("20.0\n")
        f.write("15.75\n")
        f.write("invalid\n")
        f.write("5.0\n")

def cleanup_sample_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == '__main__':
    sample_file_path = 'volume_data.txt'
    create_sample_file(sample_file_path)
    try:
        total = calculate_total_volume(sample_file_path)
        print(total)
    finally:
        cleanup_sample_file(sample_file_path)