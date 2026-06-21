def is_positive(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return number > 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, 3.14, -2.7, 5, -3, -0.01]
    results = {value: is_positive(value) for value in sample_values}
    print(results)