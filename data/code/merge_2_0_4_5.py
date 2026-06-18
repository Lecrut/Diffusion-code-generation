def check_equality(a, b):
    return a is b and isinstance(b, (int, float, str, list, dict))
if __name__ == '__main__':
    x = [1, 2, 3]
    y = [1, 2, 3]
    result = check_equality(x, y)
    print(result)