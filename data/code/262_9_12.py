import csv

def find_min_max(file_path):
    min_val = float('inf')
    max_val = float('-inf')

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                try:
                    num = float(value)
                    if num < min_val:
                        min_val = num
                    if num > max_val:
                        max_val = num
                except ValueError:
                    continue

    return min_val, max_val

if __name__ == '__main__':
    sample_file_path = 'sample.csv'
    print(find_min_max(sample_file_path))