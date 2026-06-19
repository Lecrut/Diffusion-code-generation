def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be an integer or float.")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be an integer or float.")
    return a + b

if __name__ == '__main__':
    try:
        result = sum_two_numbers(15.5, 20)
        print(result)
    except Exception as e:
        print(e)