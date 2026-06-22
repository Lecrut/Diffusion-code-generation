def has_positive_number(filename):
    try:
        with open(filename, 'r') as file:
            numbers = map(int, file.read().split())
            for number in numbers:
                if number > 0:
                    return True
        return False
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("Invalid data in the file.")
        return None

if __name__ == '__main__':
    sample_filename = 'sample_numbers.txt'
    result = has_positive_number(sample_filename)
    if result is not None:
        print(result)