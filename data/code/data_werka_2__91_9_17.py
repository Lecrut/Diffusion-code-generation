def negate_boolean(value):
    truthy = bool(value)
    negated = not truthy
    return negated

if __name__ == '__main__':
    sample_input = True
    result = negate_boolean(sample_input)
    print(result)
    sample_input = False
    result = negate_boolean(sample_input)
    print(result)