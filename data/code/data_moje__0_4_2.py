import tempfile
import os

def meters_to_yards(meters):
    return meters * 1.09361

def process_lengths_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    results = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                meters = float(line)
                yards = meters_to_yards(meters)
                results.append(yards)
            except ValueError:
                results.append(None)
    return results

if __name__ == '__main__':
    sample_values = [1.0, 100.0, 0.5, 1000.0]
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        for value in sample_values:
            f.write(f"{value}\n")
        temp_path = f.name

    try:
        results = process_lengths_from_file(temp_path)
        for result in results:
            print(result)
    finally:
        os.unlink(temp_path)