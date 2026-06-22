def sum_ten_numbers(**kwargs):
    if len(kwargs) != 10:
        raise ValueError("Exactly ten numbers must be provided.")
    return sum(kwargs.values())

if __name__ == '__main__':
    sample_values = {
        'a': 1.5,
        'b': 2.75,
        'c': 3.0,
        'd': -4.2,
        'e': 10.1,
        'f': 1.5,
        'g': 2.75,
        'h': 3.0,
        'i': -4.2,
        'j': 100.1
    }
    result = sum_ten_numbers(**sample_values)
    print(result)