def flip_boolean_values(boolean_list):
    return [not x for x in boolean_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(flip_boolean_values(sample_values))