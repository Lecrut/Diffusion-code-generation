def find_max_value_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return max(numbers)

if __name__ == '__main__':
    sample_values = '1\n2\n3\n4\n5'
    with open('sample.txt', 'w') as file:
        file.write(sample_values)
    
    max_value = find_max_value_from_file('sample.txt')
    print(max_value)