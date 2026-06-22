def check_any_true(values):
    if not values:
        return False
    for val in values:
        if val is True:
            return True
    return False

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = check_any_true(sample_values)
    print(result)