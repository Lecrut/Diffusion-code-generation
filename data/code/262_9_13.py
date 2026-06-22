import csv

class MinMaxFinder:
    def __init__(self):
        self.min_value = None
        self.max_value = None

    def update_min_max(self, value):
        if self.min_value is None or value < self.min_value:
            self.min_value = value
        if self.max_value is None or value > self.max_value:
            self.max_value = value

def process_csv(file_path, min_max_finder):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                try:
                    value = float(item)
                    min_max_finder.update_min_max(value)
                except ValueError:
                    continue

if __name__ == '__main__':
    finder = MinMaxFinder()
    process_csv('large_file.csv', finder)
    print(f"Smallest element: {finder.min_value}")
    print(f"Largest element: {finder.max_value}")