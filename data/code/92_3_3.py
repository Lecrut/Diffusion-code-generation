def negate_bools(values):
    return [not v for v in values]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    result = negate_bools(sample_values)
    print(result)