def is_positive(number):
    try:
        if isinstance(number, int):
            return number > 0
        else:
            raise ValueError("Input must be an integer.")
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_values = [10, -5, 0, 'a', None]
    for value in sample_values:
        result = is_positive(value)
        print(result)