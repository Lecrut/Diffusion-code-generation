INVERSION_KEY = True

def invert_boolean(value):
    return value ^ INVERSION_KEY

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(invert_boolean(val))