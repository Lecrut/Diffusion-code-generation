import csv

def find_min_max(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        first_row = next(reader)
        min_val = float(first_row[0])
        max_val = float(first_row[0])

        for row in reader:
            for value in row:
                num = float(value)
                if num < min_val:
                    min_val = num
                if num > max_val:
                    max_val = num

    return min_val, max_val

if __name__ == '__main__':
    sample_file_path = 'sample.csv'
    with open(sample_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([3, 1, 4, 1, 5, 9, 2, 6])
        writer.writerow([-10, 5, 20, -3, 15])

    min_val, max_val = find_min_max(sample_file_path)
    print(f"Smallest element: {min_val}, Largest element: {max_val}")