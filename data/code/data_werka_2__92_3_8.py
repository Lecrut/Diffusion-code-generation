def invert_boolean_sequence(flags):
    lookup = {True: False, False: True}
    return [lookup[val] for val in flags]

if __name__ == '__main__':
    samples = [True, True, False, False]
    print(invert_boolean_sequence(samples))