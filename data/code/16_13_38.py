def is_positive(number):
    type_map = {
        int: lambda x: x > 0,
        float: lambda x: x > 0,
    }
    
    if isinstance(number, (int, float)):
        return type_map[type(number)](number)
    else:
        raise ValueError("Input must be an integer or a float")

if __name__ == '__main__':
    sample_values = [42, -17, 2.718, -3.14, 0, 'hello', None]
    for value in sample_values:
        try:
            result = is_positive(value)
            print(f"{value}: {result}")
        except ValueError as e:
            print(f"{value}: {e}")