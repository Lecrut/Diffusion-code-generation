def are_values_equal(a: any, b: any) -> bool:
    if not isinstance(a, type(b)):
        raise TypeError('Inputs must be of the same type')
    return a == b
if __name__ == '__main__':
    x = 5
    y = 5
    print(are_values_equal(x, y))
    x = 10
    y = 3
    print(are_values_equal(x, y))
    a_val = 'hello'
    b_val = 'hello'
    print(are_values_equal(a_val, b_val))
    c_val = 'hello'
    d_val = 'world'
    print(are_values_equal(c_val, d_val))