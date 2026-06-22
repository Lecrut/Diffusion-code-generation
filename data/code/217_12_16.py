def perform_operations(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = None if y == 0 else x / y
    modulus = None if y == 0 else x % y
    return add, subtract, multiply, divide, modulus

if __name__ == '__main__':
    values = (8, 2)
    results = perform_operations(*values)
    print(results)