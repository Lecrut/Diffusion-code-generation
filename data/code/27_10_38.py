def compare_values(a, b):
    return abs(a - b) > 1e-10

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = compare_values(value1, value2)
    print(result)