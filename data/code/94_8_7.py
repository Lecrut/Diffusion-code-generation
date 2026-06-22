def has_true(values):
    if not values:
        return False
    return any(values)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = has_true(sample_list)
    print(result)