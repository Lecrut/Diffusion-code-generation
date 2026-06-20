def invert_booleans(boolean_list):
    return [not x for x in boolean_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(invert_booleans(sample_values))