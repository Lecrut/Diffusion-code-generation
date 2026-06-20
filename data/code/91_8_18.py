NEGATE_TRUE = True
NEGATE_FALSE = False

def negate_boolean(value):
    return not value
if __name__ == '__main__':
    original_value_true = NEGATE_TRUE
    negated_value_true = negate_boolean(original_value_true)
    print(f'Original: {original_value_true}, Negated: {negated_value_true}')
    original_value_false = NEGATE_FALSE
    negated_value_false = negate_boolean(original_value_false)
    print(f'Original: {original_value_false}, Negated: {negated_value_false}')