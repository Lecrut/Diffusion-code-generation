def are_values_equal(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both values must be numbers")
    return a == b

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(3, 7))