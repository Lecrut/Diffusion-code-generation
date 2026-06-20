def contains_negative(values):
    for value in values:
        if value < 0:
            return True
    return False

if __name__ == '__main__':
    test_cases = [10, -5, 0, -100, 3.14]
    print(contains_negative(test_cases))