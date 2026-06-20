def negate_boolean(value):
    return not value
if __name__ == '__main__':
    true_value = True
    false_value = False
    negated_true = negate_boolean(true_value)
    negated_false = negate_boolean(false_value)
    print(negated_true)
    print(negated_false)