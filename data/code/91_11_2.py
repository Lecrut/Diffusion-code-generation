def negate_boolean(value):
    return not value
if __name__ == '__main__':
    true_input = True
    false_input = False
    negated_true = negate_boolean(true_input)
    negated_false = negate_boolean(false_input)
    print(f"Negating True: {negated_true}")
    print(f"Negating False: {negated_false}")