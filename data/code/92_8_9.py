def invert_boolean(boolean_value):
    return not boolean_value

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        print(invert_boolean(value))