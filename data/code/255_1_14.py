def load_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    return numbers

def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    numbers = load_numbers_from_file(sample_file_path)
    largest_number = find_largest_number(numbers)
    print(largest_number)