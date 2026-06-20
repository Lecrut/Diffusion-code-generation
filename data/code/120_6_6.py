def are_values_equal(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a == b

if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal(10.5, 10.5))
    print(are_values_equal(10, 20))
    try:
        print(are_values_equal('hello', 'hello'))
    except ValueError as e:
        print(e)