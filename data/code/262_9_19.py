import csv

class MinMaxFinder:
    MIN_VALUE = float('inf')
    MAX_VALUE = float('-inf')

    @staticmethod
    def find_min_max(file_path):
        min_val = MinMaxFinder.MIN_VALUE
        max_val = MinMaxFinder.MAX_VALUE

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
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
    file_path = 'sample.csv'
    min_val, max_val = MinMaxFinder.find_min_max(file_path)
    print(f"Smallest element: {min_val}, Largest element: {max_val}")