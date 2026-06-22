def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return number > 0

if __name__ == '__main__':
    try:
        sample_values = [10, -5, 0, 3, -1, 7]
        results = {value: is_positive(value) for value in sample_values}
        print(results)
    except ValueError as e:
        print(e)