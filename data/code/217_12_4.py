def compare_numbers(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = None if b == 0 else a / b
    modulus = None if b == 0 else a % b
    return add, subtract, multiply, divide, modulus

if __name__ == '__main__':
    result = compare_numbers(10, 5)
    print(result)