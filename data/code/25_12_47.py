def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    raise ValueError("Unsupported type")

if __name__ == '__main__':
    test_values = [
        0,
        1,
        -0.0,
        0.001,
        0.0,
        1e-308,
        '0'
    ]
    
    for val in test_values:
        try:
            print(is_zero(val))
        except ValueError as e:
            print(e)