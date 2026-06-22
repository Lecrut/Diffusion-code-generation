TRUE_MAP = {True: 1, False: 0}

def check_any_true(values):
    return sum(TRUE_MAP.get(v, 0) for v in values) > 0

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = check_any_true(sample_values)
    print(result)