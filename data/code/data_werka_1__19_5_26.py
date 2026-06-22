def has_positive_number(filename):
    try:
        with open(filename, 'r') as file:
            numbers = map(int, file.readlines())
            for number in numbers:
                if number > 0:
                    return True
            return False
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid number format in the file.")

if __name__ == '__main__':
    sample_filename = "sample_numbers.txt"
    result = has_positive_number(sample_filename)
    print(result)