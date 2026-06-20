def negate_boolean(value):
    return not value

if __name__ == '__main__':
    original_value = True
    negated_value = negate_boolean(original_value)
    print(f"Original: {original_value}, Negated: {negated_value}")