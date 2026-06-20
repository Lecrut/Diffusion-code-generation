def flip_boolean_values(boolean_list):
    return [not b for b in boolean_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    inverted_values = flip_boolean_values(sample_values)
    print(inverted_values)