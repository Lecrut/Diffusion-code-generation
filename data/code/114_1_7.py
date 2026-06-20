def multiply_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a * b

if __name__ == '__main__':
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    result = multiply_two_numbers(num1, num2)
    print(result)