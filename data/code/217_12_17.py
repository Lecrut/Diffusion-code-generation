def compare_numbers(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b if b != 0 else None
    modulus = a % b if b != 0 else None
    return (add, subtract, multiply, divide, modulus)

if __name__ == '__main__':
    result = compare_numbers(10, 5)
    print(result)