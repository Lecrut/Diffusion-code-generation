TRUE = True

def invert_boolean(value):
    return value ^ TRUE
if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(invert_boolean(val))