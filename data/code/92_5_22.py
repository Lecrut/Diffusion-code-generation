def invert_booleans(values):
    for value in values:
        yield not value

if __name__ == '__main__':
    test_values = [False, True, False, True]
    inverted_results = list(invert_booleans(test_values))
    print(inverted_results)