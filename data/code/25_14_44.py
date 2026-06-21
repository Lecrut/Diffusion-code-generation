def is_zero(value):
    type_map = {
        int: lambda v: v == 0,
        float: lambda v: v == 0.0,
        complex: lambda v: v == 0 + 0j,
    }
    
    value_type = type(value)
    if value_type in type_map:
        return type_map[value_type](value)
    else:
        raise ValueError('Unsupported data type')

if __name__ == '__main__':
    test_values = [0, 0.0, 0 + 0j, 1, 1.5, 1 + 2j, '0', '', None]
    for value in test_values:
        try:
            print(f"is_zero({value}): {is_zero(value)}")
        except ValueError as e:
            print(f"is_zero({value}): {e}")