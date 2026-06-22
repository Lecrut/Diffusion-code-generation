def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def add_numbers(a, b):
    if not is_numeric(a) or not is_numeric(b):
        raise ValueError("Both inputs must be numeric.")
    return a + b

if __name__ == '__main__':
    result1 = add_numbers(5, 10)
    print(result1)

    try:
        result2 = add_numbers('a', 10)
        print(result2)
    except ValueError as e:
        print(e)

    result3 = add_numbers(-3.5, 7.8)
    print(result3)