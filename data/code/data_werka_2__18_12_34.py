def is_greater(a, b):
    return a > b

if __name__ == '__main__':
    TEST_VALUES = [
        (10, 5),
        (3, 7),
        (8, 8),
        (-1, -2),
        (7, 7)
    ]
    
    for value_pair in TEST_VALUES:
        result = is_greater(*value_pair)
        print(result)