def invert_boolean(value):
    return value ^ True

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        inverted_val = invert_boolean(val)
        print(f"Original: {val}, Inverted: {inverted_val}")