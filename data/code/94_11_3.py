def check_any_true(values):
    lookup = {True: 1, False: 0}
    mapped = [lookup.get(v, 0) for v in values]
    return sum(mapped) > 0

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = check_any_true(sample_values)
    print(result)