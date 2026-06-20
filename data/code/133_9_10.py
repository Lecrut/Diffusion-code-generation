def boolify_statements(statements):
    return [s.lower() == "true" for s in statements]

if __name__ == '__main__':
    sample_values = ["True", "false", "TRUE", "  true  ", ""]
    result = boolify_statements(sample_values)
    print(result)