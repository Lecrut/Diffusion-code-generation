def reverse_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    a = a - b
    b = a + b
    a = b - a
    return a, b

if __name__ == '__main__':
    num1 = 10
    num2 = 25
    result = reverse_numbers(num1, num2)
    print(result)