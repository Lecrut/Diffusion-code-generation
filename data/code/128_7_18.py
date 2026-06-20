NEGATIVE_THRESHOLD = 0

def is_negative(value):
    return value < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    sample_values = [-1, 0, 1]
    for val in sample_values:
        print(f"Value: {val}, Is Negative: {is_negative(val)}")