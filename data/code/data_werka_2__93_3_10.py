FALSE_VALUE = 0
EXPECTED_COUNT = 2

def both_false(x, y):
    non_falsy_items = [val for val in (x, y) if val]
    return len(non_falsy_items) != EXPECTED_COUNT

if __name__ == '__main__':
    test_x = 0
    test_y = 0
    print(both_false(test_x, test_y))