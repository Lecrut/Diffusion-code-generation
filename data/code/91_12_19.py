def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    original_value1 = True
    negated_value1 = negate_boolean(original_value1)
    print(f"Negated {original_value1}: {negated_value1}")

    original_value2 = False
    negated_value2 = negate_boolean(original_value2)
    print(f"Negated {original_value2}: {negated_value2}")