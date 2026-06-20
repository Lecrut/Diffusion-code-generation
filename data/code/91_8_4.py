def negate_boolean(value):
    return not value

if __name__ == '__main__':
    original_true = True
    negated_true = negate_boolean(original_true)
    print(f"Original: {original_true}, Negated: {negated_true}")

    original_false = False
    negated_false = negate_boolean(original_false)
    print(f"Original: {original_false}, Negated: {negated_false}")