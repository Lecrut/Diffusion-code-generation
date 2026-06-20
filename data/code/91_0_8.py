def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    print(f"Original value: {sample_true}, Negated value: {negate_boolean(sample_true)}")
    print(f"Original value: {sample_false}, Negated value: {negate_boolean(sample_false)}")