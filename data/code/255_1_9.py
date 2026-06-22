class NumberFinder:
    @staticmethod
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

    @staticmethod
    def find_maximum(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        current_max = max(numbers)
        return current_max

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    numbers = NumberFinder.read_numbers_from_file(sample_file_path)
    maximum_value = NumberFinder.find_maximum(numbers)
    print(maximum_value)