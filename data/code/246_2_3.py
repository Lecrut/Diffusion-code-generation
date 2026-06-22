def add_two_numbers(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floats")
    return a + b

if __name__ == '__main__':
    num1 = 3.5
    num2 = 2.5
    result = add_two_numbers(num1, num2)
    print(result)