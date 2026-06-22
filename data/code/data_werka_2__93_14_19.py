from functools import reduce

FALSE_VALUE = False

def validate_false_pair(condition_a, condition_b):
    inputs = [condition_a, condition_b]
    return reduce(lambda acc, val: acc and (val is FALSE_VALUE), inputs, True)

if __name__ == '__main__':
    a_sample = False
    b_sample = False
    computed_value = validate_false_pair(a_sample, b_sample)
    print(computed_value)