def check_negativity(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return number < 0

if __name__ == '__main__':
    sample_values = [42, -17, 0, -2.718, 3.14]
    results = {value: check_negativity(value) for value in sample_values}
    print(results)