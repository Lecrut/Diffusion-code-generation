def opposite_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        print(opposite_boolean(val))