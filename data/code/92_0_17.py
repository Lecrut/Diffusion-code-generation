def invert_boolean(value):
    return not value

if __name__ == '__main__':
    sample_value = True
    inverted_value = invert_boolean(sample_value)
    print(inverted_value)
    another_sample = False
    another_inverted = invert_boolean(another_sample)
    print(another_inverted)