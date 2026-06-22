def find_max_value(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    return max(numbers)

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    maximum_value = find_max_value(sample_file_path)
    print(maximum_value)