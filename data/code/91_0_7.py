def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_value = False
    negated_sample = negate_boolean(sample_value)
    print(f"Original value: {sample_value}")
    print(f"Negated value: {negated_sample}")