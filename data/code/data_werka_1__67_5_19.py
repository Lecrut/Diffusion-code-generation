def add_numbers(a, b):
    try:
        result = float(a) + float(b)
        return result
    except ValueError:
        raise TypeError("Both inputs must be numbers")

if __name__ == '__main__':
    print(add_numbers(5, 10))
    print(add_numbers(20.5, 30.2))
    try:
        print(add_numbers('a', 10))
    except TypeError as e:
        print(e)
    try:
        print(add_numbers(15, 'b'))
    except TypeError as e:
        print(e)