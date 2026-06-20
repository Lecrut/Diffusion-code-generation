def are_values_equal(a: any, b: any) -> bool:
    if not (isinstance(a, type(b)) or isinstance(b, type(a))):
        raise ValueError("Types of the two values must be the same.")
    return a == b

if __name__ == '__main__':
    x = 5
    y = 5
    print(are_values_equal(x, y))
    
    x = 10
    y = 3
    print(are_values_equal(x, y))