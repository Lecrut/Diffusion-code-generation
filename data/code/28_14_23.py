def compare_values(a, b):
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("Both inputs must be numbers (int or float).")
    return a > b

if __name__ == '__main__':
    value1 = 3.14
    value2 = 2.71
    result = compare_values(value1, value2)
    print(result)