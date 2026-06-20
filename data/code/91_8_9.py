def negate_boolean(value):
    return not value

if __name__ == '__main__':
    original_value_true = True
    negated_value_true = negate_boolean(original_value_true)
    print(f"Original: {original_value_true}, Negated: {negated_value_true}")

    original_value_false = False
    negated_value_false = negate_boolean(original_value_false)
    print(f"Original: {original_value_false}, Negated: {negated_value_false}")