def is_negative(value):
    return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, -2.71, 'hello', None, -0]
    results = {val: is_negative(val) for val in sample_values}
    print(results)