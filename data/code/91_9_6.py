def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value.")
    return not value

if __name__ == '__main__':
    original_value = True
    negated_value = negate_boolean(original_value)
    print(f"Original value: {original_value}")
    print(f"Negated value: {negated_value}")

    original_value = False
    negated_value = negate_boolean(original_value)
    print(f"Original value: {original_value}")
    print(f"Negated value: {negated_value}")