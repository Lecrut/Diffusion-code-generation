def negate_boolean(value):
    return not value

if __name__ == '__main__':
    original_values = [True, False]
    for val in original_values:
        negated_value = negate_boolean(val)
        print(f"Original value: {val}, Negated value: {negated_value}")