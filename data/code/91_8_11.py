def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_value = True
    original_value = sample_value
    negated_value = negate_boolean(original_value)
    print(f"Original: {original_value}, Negated: {negated_value}")