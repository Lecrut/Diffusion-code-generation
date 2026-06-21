def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 3.14, None, 'hello', [], {}]
    for value in test_values:
        print(f"is_zero({value}): {is_zero(value)}")