def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    return numbers

def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    current_max = max(numbers)
    return current_max

class MaxFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.numbers = []

    def load_numbers(self):
        self.numbers = read_numbers_from_file(self.file_path)

    def find_and_print_maximum(self):
        self.load_numbers()
        max_value = find_maximum(self.numbers)
        print(max_value)

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    finder = MaxFinder(sample_file_path)
    finder.find_and_print_maximum()