def is_negative(value):
    return value < 0

if __name__ == '__main__':
    SAMPLE_VALUES = [42, -17, 0, -0.5, 3.14159]
    for val in SAMPLE_VALUES:
        print(is_negative(val))