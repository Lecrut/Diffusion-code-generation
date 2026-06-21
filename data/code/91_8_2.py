def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        negated = negate_boolean(val)
        print(f"Original: {val}, Negated: {negated}")