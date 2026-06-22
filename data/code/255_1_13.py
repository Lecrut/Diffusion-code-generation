MAX_VALUE_NOT_FOUND = "No numbers found in file"

def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = int(line.strip())
                numbers.append(number)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError:
        print("Skipping invalid line")
    return numbers

def find_maximum(numbers):
    if not numbers:
        raise ValueError(MAX_VALUE_NOT_FOUND)
    return max(numbers)

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    numbers = read_numbers_from_file(sample_file_path)
    try:
        maximum_value = find_maximum(numbers)
        print(maximum_value)
    except ValueError as e:
        print(e)