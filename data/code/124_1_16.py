def basic_arithmetic(a, b):
    results = {}
    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b
    results['floor_division'] = a // b
    return results

if __name__ == '__main__':
    result = basic_arithmetic(10, 4)
    print(result)