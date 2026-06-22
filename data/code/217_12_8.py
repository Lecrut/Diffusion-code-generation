def compare_numbers(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else None

if __name__ == '__main__':
    result = compare_numbers(10, 5)
    print(result)