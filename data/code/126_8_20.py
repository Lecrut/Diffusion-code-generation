def are_values_equal(a, b):
    if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
        raise ValueError("Both inputs must be int, float, or str")
    return a == b

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(3, 7))