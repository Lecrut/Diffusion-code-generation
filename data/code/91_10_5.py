NEGATE_TRUE = True
NEGATE_FALSE = False

def negate_boolean(bool_val):
    return not bool_val
if __name__ == '__main__':
    sample_value_1 = NEGATE_TRUE
    sample_value_2 = NEGATE_FALSE
    print(negate_boolean(sample_value_1))
    print(negate_boolean(sample_value_2))