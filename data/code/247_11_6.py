def add_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = add_numbers(num1, num2)
    print(result)