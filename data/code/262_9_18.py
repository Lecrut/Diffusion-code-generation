import csv

def find_min_max(file_path):
    min_val = float('inf')
    max_val = float('-inf')

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row:
                try:
                    num = float(item)
                    if num < min_val:
                        min_val = num
                    if num > max_val:
                        max_val = num
                except ValueError:
                    continue

    return min_val, max_val

if __name__ == '__main__':
    file_path = 'large_file.csv'
    min_val, max_val = find_min_max(file_path)
    print(f"Smallest element: {min_val}, Largest element: {max_val}")