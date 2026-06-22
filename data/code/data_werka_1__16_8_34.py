def is_positive(number):
    try:
        if int(number) > 0:
            return True
        else:
            return False
    except ValueError:
        return "Invalid input. Please enter an integer."

if __name__ == '__main__':
    sample_values = [10, -5, 'abc', 0]
    for value in sample_values:
        result = is_positive(value)
        print(result)