def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return number > 0

if __name__ == '__main__':
    try:
        sample_values = [15, -3, 0, 8, -7, 2]
        results = {value: is_positive(value) for value in sample_values}
        print(results)
    except ValueError as e:
        print(e)