def has_positive_number(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = map(int, file.readlines())
            for number in numbers:
                if number > 0:
                    return True
        return False
    except FileNotFoundError:
        print('File not found')
        return False
    except ValueError:
        print('Invalid data in the file')
        return False
if __name__ == '__main__':
    sample_data = '1\n-2\n3\n-4'
    with open('sample_numbers.txt', 'w') as f:
        f.write(sample_data)
    result = has_positive_number('sample_numbers.txt')
    print(result)