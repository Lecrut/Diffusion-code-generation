def add_numbers(a, b):
    try:
        return float(a) + float(b)
    except ValueError as e:
        raise TypeError("Both inputs must be numbers") from e

if __name__ == '__main__':
    result1 = add_numbers(5, 10)
    print(result1)

    result2 = add_numbers(20.5, 30.75)
    print(result2)

    try:
        result3 = add_numbers('a', 10)
    except TypeError as e:
        print(e)

    try:
        result4 = add_numbers(10, 'b')
    except TypeError as e:
        print(e)