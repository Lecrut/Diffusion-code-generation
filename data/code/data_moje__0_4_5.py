def meters_to_yards(meters):
    return meters * 1.09361

def process_lengths_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lengths = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                meter_value = float(line)
                yards_value = meters_to_yards(meter_value)
                lengths.append(yards_value)
            except ValueError:
                continue
    return lengths

def convert_sample():
    sample_meters = [1.0, 100.0, 0.5, 10.0]
    results = []
    for m in sample_meters:
        results.append(meters_to_yards(m))
    return results

if __name__ == '__main__':
    print(convert_sample())