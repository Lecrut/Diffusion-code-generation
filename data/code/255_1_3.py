def find_max_value(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return max(numbers)

if __name__ == '__main__':
    print(find_max_value('sample_numbers.txt'))