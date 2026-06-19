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
        return False
    except ValueError:
        print("Invalid data in the file.")
        return False

if __name__ == '__main__':
    sample_filename = 'numbers.txt'
    result = has_positive_number(sample_filename)
    print(result)