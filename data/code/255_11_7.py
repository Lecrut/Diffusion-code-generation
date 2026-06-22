def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping non-numeric value: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return numbers

def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = numbers[0]
    for number in numbers[1:]:
        if number > max_val:
            max_val = number
    return max_val

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    sample_numbers = read_numbers_from_file(sample_file_path)
    try:
        maximum_value = find_maximum(sample_numbers)
        print(f"The maximum value is: {maximum_value}")
    except ValueError as e:
        print(e)