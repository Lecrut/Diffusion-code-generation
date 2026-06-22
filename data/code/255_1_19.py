class MaxFinder:
    def __init__(self):
        self.max_value = None

    def read_numbers_from_file(self, file_path):
        numbers = []
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
        return numbers

    def find_maximum(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        self.max_value = max(numbers)

if __name__ == '__main__':
    finder = MaxFinder()
    sample_file_path = 'sample_numbers.txt'
    numbers = finder.read_numbers_from_file(sample_file_path)
    finder.find_maximum(numbers)
    print(finder.max_value)