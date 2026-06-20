def is_greater(x, y):
    return x > y

if __name__ == '__main__':
    test_cases = [(5, 3), (2, 4)]
    for x, y in test_cases:
        result = is_greater(x, y)
        print(f"x: {x}, y: {y}, is_greater: {result}")