def multiply_numbers(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers.")
    return a * b

if __name__ == '__main__':
    num1 = 3.141592653589793
    num2 = 2.718281828459045
    result = multiply_numbers(num1, num2)
    print(result)