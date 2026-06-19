def is_positive(number):
    try:
        if int(number) > 0:
            return True
        else:
            return False
    except ValueError:
        return "Error: Input is not an integer."

if __name__ == '__main__':
    sample_values = [5, -3, 'a', 0]
    for value in sample_values:
        result = is_positive(value)
        print(result)