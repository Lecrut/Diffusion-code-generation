def is_greater(a, b):
    return a > b

if __name__ == '__main__':
    TEST_VALUES = [
        (10, 5),
        (3, 7),
        (8, 8),
        (-1, -2),
        (7, 7),
        (0, -1),
        (5.5, 5.4),
        (5.4, 5.5)
    ]
    
    for a, b in TEST_VALUES:
        print(is_greater(a, b))