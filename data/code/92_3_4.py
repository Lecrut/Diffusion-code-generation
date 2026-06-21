def negate_boolean_list(values):
    return [not val for val in values]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    result = negate_boolean_list(sample_values)
    print(result)