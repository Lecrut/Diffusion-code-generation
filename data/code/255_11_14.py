class MaxFinder:
    @staticmethod
    def read_numbers_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                numbers = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
            return numbers
        except FileNotFoundError:
            print(f"Error: The file {file_path} does not exist.")
            return []
        except ValueError:
            print("Error: The file contains non-numeric data.")
            return []

    @staticmethod
    def find_maximum(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        max_val = numbers[0]
        for x in numbers[1:]:
            if x > max_val:
                max_val = x
        return max_val

if __name__ == '__main__':
    file_path = 'numbers.txt'
    numbers = MaxFinder.read_numbers_from_file(file_path)
    if numbers:
        print(f"The maximum value is: {MaxFinder.find_maximum(numbers)}")