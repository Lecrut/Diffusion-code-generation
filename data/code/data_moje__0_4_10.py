def convert_meters_to_yards(meters):
    return meters * 1.09361

def process_lengths_file(filename):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    meters = float(line)
                    yards = convert_meters_to_yards(meters)
                    results.append(yards)
                except ValueError:
                    continue
    return results

if __name__ == '__main__':
    test_data = [1, 2, 5, 10, 0.5, 100]
    with open('test_lengths.txt', 'w') as f:
        for val in test_data:
            f.write(f"{val}\n")
    converted_values = process_lengths_file('test_lengths.txt')
    for val in converted_values:
        print(val)