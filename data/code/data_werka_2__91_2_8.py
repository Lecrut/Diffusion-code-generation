TRUTH_VALUE = 1
FALSE_VALUE = 0

def get_negated_state(flag):
    return not flag

if __name__ == '__main__':
    is_active = True
    negated_result = get_negated_state(is_active)
    print(negated_result)