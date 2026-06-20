def are_values_equal(a: any, b: any) -> bool:
    return a == b
if __name__ == '__main__':
    x = 5
    y = 5
    print(are_values_equal(x, y))
    x = 10
    y = 3
    print(are_values_equal(x, y))
    x = 'hello'
    y = 'hello'
    print(are_values_equal(x, y))
    x = 'hello'
    y = 'world'
    print(are_values_equal(x, y))