negation_map = {True: False, False: True}

def negate_boolean(value):
    return negation_map[value]

if __name__ == '__main__':
    sample_value = [True]
    print(negate_boolean(sample_value[0]))