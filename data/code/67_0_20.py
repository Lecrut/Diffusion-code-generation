def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be integers or floats.")
    return a + b

if __name__ == '__main__':
    SAMPLE_FIRST_VALUE = 15
    SAMPLE_SECOND_VALUE = 25
    result = sum_two_numbers(SAMPLE_FIRST_VALUE, SAMPLE_SECOND_VALUE)
    print(result)