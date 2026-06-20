def negate_boolean(boolean_value):
    return not boolean_value

if __name__ == '__main__':
    sample_values = {True: False, False: True}
    for original, expected in sample_values.items():
        result = negate_boolean(original)
        print(f"Original value: {original}, Negated value: {result}, Expected: {expected}")