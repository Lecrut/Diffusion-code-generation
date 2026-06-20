def are_values_equal(a, b):
    if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
        raise ValueError("Both values must be integers, floats, or strings.")
    return a == b

if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal(10.5, 10.5))
    print(are_values_equal('hello', 'hello'))
    print(are_values_equal('hello', 'world'))
    try:
        print(are_values_equal([1, 2], [1, 2]))
    except ValueError as e:
        print(e)