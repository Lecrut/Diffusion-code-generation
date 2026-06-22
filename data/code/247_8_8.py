def sum_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    value1 = 10
    value2 = 5
    result = sum_two_numbers(value1, value2)
    print(result)