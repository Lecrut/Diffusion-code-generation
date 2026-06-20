NEGATIVITY_THRESHOLD = 0

def is_negative(value):
    return value < NEGATIVITY_THRESHOLD

if __name__ == '__main__':
    sample_values = [10, -5, 0, -100, 3.14]
    for value in sample_values:
        result = is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")