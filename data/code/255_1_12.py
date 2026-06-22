class NumberProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_numbers_from_file(self):
        numbers = []
        with open(self.file_path, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
        return numbers

    def find_maximum(self):
        numbers = self.read_numbers_from_file()
        if not numbers:
            raise ValueError("Input list cannot be empty")
        current_max = max(numbers)
        return current_max

if __name__ == '__main__':
    processor = NumberProcessor('sample_numbers.txt')
    maximum_value = processor.find_maximum()
    print(maximum_value)