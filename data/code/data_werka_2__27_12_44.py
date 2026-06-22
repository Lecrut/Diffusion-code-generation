def check_inequality(value1, value2):
    if type(value1) != type(value2):
        return True
    return value1 != value2

if __name__ == '__main__':
    sample_values = [
        (5, 10),
        ('hello', 'world'),
        (3.14, 3.14),
        ([1, 2, 3], [1, 2, 3]),
        (True, False),
        (None, None)
    ]

    for value1, value2 in sample_values:
        result = check_inequality(value1, value2)
        print(f"check_inequality({value1}, {value2}) = {result}")