NEGATIVE_THRESHOLD = 0

def contains_negative(values):
    for value in values:
        if value < NEGATIVE_THRESHOLD:
            return True
    return False

if __name__ == '__main__':
    test_values = [1, -2, 3, -4, 5, -6, 0]
    print(contains_negative(test_values))