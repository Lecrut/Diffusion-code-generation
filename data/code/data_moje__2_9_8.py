import csv
import io
import os

def calculate_total_volume(file_content: str) -> float:
    total = 0.0
    reader = csv.DictReader(io.StringIO(file_content))
    for row in reader:
        try:
            volume = float(row['volume'])
            total += volume
        except (ValueError, KeyError):
            continue
    return total

def create_sample_file():
    data = "volume\n10.5\n20.0\nabc\n30.25\n"
    filename = "volumes.csv"
    with open(filename, 'w', newline='') as f:
        f.write(data)
    return filename

if __name__ == '__main__':
    filename = create_sample_file()
    try:
        with open(filename, 'r') as f:
            content = f.read()
        result = calculate_total_volume(content)
        print(result)
    finally:
        if os.path.exists(filename):
            os.remove(filename)