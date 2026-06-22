def meters_to_yards(lengths):
    return [m * 1.09361 for m in lengths]

def read_lengths_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lengths = []
    for line in lines:
        try:
            lengths.append(float(line.strip()))
        except ValueError:
            continue
    return lengths

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 3.0, 10.0]
    yards = meters_to_yards(sample_lengths)
    print(yards)