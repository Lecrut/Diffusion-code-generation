def negate_boolean(value):
    return not value

if __name__ == '__main__':
    original = True
    negated = negate_boolean(original)
    print(f"Original: {original}")
    print(f"Negated: {negated}")