def negate_bools(values):
    return [not v for v in values]

if __name__ == '__main__':
    sample = [True, False, True, False]
    result = negate_bools(sample)
    print(result)