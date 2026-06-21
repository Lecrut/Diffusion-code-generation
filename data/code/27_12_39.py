def check_inequality(a, b):
    type_map = {
        int: lambda x, y: x != y,
        float: lambda x, y: x != y,
        str: lambda x, y: x != y,
        list: lambda x, y: x != y,
        dict: lambda x, y: x != y,
        bool: lambda x, y: x != y,
        type(None): lambda x, y: x is not y,
        complex: lambda x, y: x != y
    }
    
    a_type = type(a)
    b_type = type(b)
    
    if a_type != b_type:
        return True
    
    if a_type in type_map:
        return type_map[a_type](a, b)
    else:
        raise ValueError(f"Unsupported type: {a_type}")

if __name__ == '__main__':
    sample_values = [
        (5, 10),
        (5.0, 10.0),
        ('hello', 'world'),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        (True, False),
        (None, None),
        (1 + 2j, 3 + 4j)
    ]
    
    for a, b in sample_values:
        result = check_inequality(a, b)
        print(f"check_inequality({a!r}, {b!r}) = {result}")