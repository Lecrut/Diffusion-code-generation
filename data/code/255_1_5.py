def find_max_value_from_file(file_path):
    max_value = None
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            if max_value is None or number > max_value:
                max_value = number
    return max_value

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    result = find_max_value_from_file(sample_file_path)
    print(result)