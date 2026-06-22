def has_positive_number(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = float(line.strip())
                if number > 0:
                    return True
        return False
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("Invalid number format.")
        return None

if __name__ == '__main__':
    sample_filename = 'numbers.txt'
    result = has_positive_number(sample_filename)
    if result is True:
        print("At least one positive number exists in the file.")
    elif result is False:
        print("No positive numbers found in the file.")
    else:
        print("An error occurred while processing the file.")