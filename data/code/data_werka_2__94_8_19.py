def any_true(values):
    if not values:
        return False
    return any(values)

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = any_true(sample_values)
    print(result)