def compare_values(a, b):
    if not isinstance(a, float) or not isinstance(b, float):
        raise ValueError("Both inputs must be floats.")
    return a > b

if __name__ == '__main__':
    value1 = 3.5
    value2 = 2.8
    result = compare_values(value1, value2)
    print(result)