NEGATIVE_THRESHOLD = 0

def is_negative(number):
    return number < NEGATIVE_THRESHOLD
if __name__ == '__main__':
    test_values = [-3, 0, 2.5, -100]
    results = [is_negative(value) for value in test_values]
    print(results)