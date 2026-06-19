def contains_positive_number(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = map(float, line.split())
                if any(num > 0 for num in numbers):
                    return True
        return False
    except IOError:
        return None

if __name__ == '__main__':
    sample_file_content = """-1 -2 -3
4 5 6
-7 -8 -9"""
    with open('sample_numbers.txt', 'w') as file:
        file.write(sample_file_content)
    
    result = contains_positive_number('sample_numbers.txt')
    print(result)