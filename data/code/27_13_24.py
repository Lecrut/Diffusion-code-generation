def check_inequality(a, b):
    return type(a) is type(b) and a != b

if __name__ == '__main__':
    value1 = 42
    value2 = "42"
    result = check_inequality(value1, value2)
    print(result)