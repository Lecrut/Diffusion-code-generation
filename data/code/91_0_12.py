def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    print(f"Negation of {sample_true}: {negate_boolean(sample_true)}")
    print(f"Negation of {sample_false}: {negate_boolean(sample_false)}")