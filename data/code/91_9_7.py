def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    original_value = True
    try:
        negated_value = negate_boolean(original_value)
        print(f"Original value: {original_value}")
        print(f"Negated value: {negated_value}")
    except ValueError as e:
        print(e)

    original_value = False
    try:
        negated_value = negate_boolean(original_value)
        print(f"Original value: {original_value}")
        print(f"Negated value: {negated_value}")
    except ValueError as e:
        print(e)