def perform_operations(a, b):
    return a + b, a - b, a * b, (a / b if b != 0 else 'undefined'), (a % b if b != 0 else 'undefined')

if __name__ == '__main__':
    result = perform_operations(10, 5)
    print(result)