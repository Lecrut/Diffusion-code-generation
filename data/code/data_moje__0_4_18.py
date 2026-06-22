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
                meter_value = float(line)
                yard_value = meters_to_yards(meter_value)
                results.append(yard_value)
            except ValueError:
                results.append(None)
    return results

if __name__ == '__main__':
    import tempfile
    import os

    sample_lengths = [1.0, 100.0, 0.5, 25.0]

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        for length in sample_lengths:
            f.write(f"{length}\n")
        temp_path = f.name

    try:
        results = process_lengths_from_file(temp_path)
        for result in results:
            print(result)
    finally:
        os.unlink(temp_path)