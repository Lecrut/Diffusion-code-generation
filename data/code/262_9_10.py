import csv

def find_min_max(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        min_val = float('inf')
        max_val = float('-inf')
        for row in reader:
            num = float(row[0])
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
    return (min_val, max_val)
if __name__ == '__main__':
    sample_file_path = 'sample.csv'
    print(find_min_max(sample_file_path))