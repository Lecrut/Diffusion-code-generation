def negate_boolean(boolean_value):
    return not boolean_value

if __name__ == '__main__':
    sample_value = True
    negated_sample = negate_boolean(sample_value)
    print(f"Original value: {sample_value}")
    print(f"Negated value: {negated_sample}")