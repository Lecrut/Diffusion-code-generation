import csv

def find_min_max(file_path):
    min_val = float('inf')
    max_val = float('-inf')
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            for value in row:
                try:
                    num = float(value)
                    min_val = min(min_val, num)
                    max_val = max(max_val, num)
                except ValueError:
                    continue
    return (min_val, max_val)
if __name__ == '__main__':
    sample_file_path = 'path_to_your_large_csv.csv'
    min_value, max_value = find_min_max(sample_file_path)
    print(f'Minimum value: {min_value}')
    print(f'Maximum value: {max_value}')