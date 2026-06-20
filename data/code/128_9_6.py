NEGATIVE_THRESHOLD = 0

def is_negative(value):
    return value < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    test_values = [-10, 5, 0, -3, 2]
    for val in test_values:
        print(f"Value {val} is negative: {is_negative(val)}")