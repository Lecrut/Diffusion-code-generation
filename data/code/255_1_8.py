def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    current_max = data[0]
    for number in data:
        if number > current_max:
            current_max = number
    return current_max

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

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    numbers = read_numbers_from_file(sample_file_path)
    maximum_value = find_maximum(numbers)
    print(maximum_value)