def is_zero(value):
    type_checks = {
        int: lambda x: x == 0,
        float: lambda x: x == 0.0,
        complex: lambda x: x == 0 + 0j,
    }
    
    value_type = type(value)
    if value_type in type_checks:
        return type_checks[value_type](value)
    else:
        raise ValueError('Unsupported data type')

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(0 + 0j))
    print(is_zero(1))
    print(is_zero(1.5))
    print(is_zero(1 + 2j))