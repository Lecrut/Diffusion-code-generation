NEGATE_TRUE = True
NEGATE_FALSE = False

def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_value = NEGATE_TRUE
    negated_value = negate_boolean(sample_value)
    print(negated_value)

    sample_value = NEGATE_FALSE
    negated_value = negate_boolean(sample_value)
    print(negated_value)