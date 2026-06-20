def compare_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both values must be integers or floats')
    return a == b
if __name__ == '__main__':
    try:
        x = 5
        y = 5
        result1 = compare_values(x, y)
        print(result1)
        x = 10
        y = 3
        result2 = compare_values(x, y)
        print(result2)
        x = 'hello'
        y = 'world'
        result3 = compare_values(x, y)
    except ValueError as e:
        print(e)