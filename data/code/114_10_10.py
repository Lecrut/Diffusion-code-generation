def multiply_two_numbers(a, b):
    if not all(isinstance(i, int) for i in [a, b]):
        raise ValueError("Both inputs must be integers.")
    return a * b

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = multiply_two_numbers(num1, num2)
    print(result)