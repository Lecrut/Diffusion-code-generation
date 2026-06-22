def compare_numbers(a, b):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else None,
        'modulus': a % b if b != 0 else None
    }

if __name__ == '__main__':
    result = compare_numbers(10, 5)
    print(result)