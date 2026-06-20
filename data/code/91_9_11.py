def negate_boolean(value):
    return not value

if __name__ == '__main__':
    original_value = True
    negated_value = negate_boolean(original_value)
    print(f"Original value: {original_value}")
    print(f"Negated value: {negated_value}")

    another_original = False
    another_negated = negate_boolean(another_original)
    print(f"Another original value: {another_original}")
    print(f"Another negated value: {another_negated}")