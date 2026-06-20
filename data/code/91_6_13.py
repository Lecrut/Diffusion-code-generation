def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_values = {True: False, False: True}
    for original, expected in sample_values.items():
        result = negate_boolean(original)
        print(f"Original: {original}, Expected Negation: {expected}, Result: {result}")