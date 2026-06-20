def negate_boolean(value):
    return not value
if __name__ == '__main__':
    TRUE = True
    FALSE = False
    sample_true = TRUE
    print(f'Original: {sample_true}, Negated: {negate_boolean(sample_true)}')
    sample_false = FALSE
    print(f'Original: {sample_false}, Negated: {negate_boolean(sample_false)}')