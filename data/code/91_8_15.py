NEGATE_FACTOR = -1

def negate_boolean(value):
    return not value
if __name__ == '__main__':
    sample_value_true = True
    print(f'Original: {sample_value_true}, Negated: {negate_boolean(sample_value_true)}')
    sample_value_false = False
    print(f'Original: {sample_value_false}, Negated: {negate_boolean(sample_value_false)}')