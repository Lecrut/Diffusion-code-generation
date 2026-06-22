class MaxFinder:
    def __init__(self):
        self.max_value = None

    def update_max(self, value):
        if self.max_value is None or value > self.max_value:
            self.max_value = value

    def get_max(self):
        return self.max_value

def read_numbers_from_file(file_path):
    max_finder = MaxFinder()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    max_finder.update_max(number)
                except ValueError:
                    print(f"Skipping non-numeric value: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return max_finder.get_max()

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    max_value = read_numbers_from_file(sample_file_path)
    print(max_value)