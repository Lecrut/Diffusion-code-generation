def is_positive(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return number > 0

if __name__ == '__main__':
    sample_values = [25, -15, 0, 7, -3]
    results = {value: is_positive(value) for value in sample_values}
    print(results)