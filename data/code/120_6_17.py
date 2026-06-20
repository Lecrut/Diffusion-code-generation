def are_values_equal(a, b):
    if not isinstance(a, type(b)):
        return False
    return a == b
if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal(10, 20))
    print(are_values_equal('hello', 'hello'))
    print(are_values_equal('hello', 'world'))