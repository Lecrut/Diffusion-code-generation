def negate_boolean(value: bool) -> bool:
    return not value
if __name__ == '__main__':
    sample_true = True
    sample_false = False
    negated_true = negate_boolean(sample_true)
    negated_false = negate_boolean(sample_false)
    print(f"Negation of {sample_true}: {negated_true}")
    print(f"Negation of {sample_false}: {negated_false}")