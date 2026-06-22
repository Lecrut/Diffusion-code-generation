def check_any_true(values):
    TRUE_SENTINEL = True
    FALSE_SENTINEL = False
    if not values:
        return FALSE_SENTINEL
    for val in values:
        if val is TRUE_SENTINEL:
            return TRUE_SENTINEL
    return FALSE_SENTINEL

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    result = check_any_true(sample_data)
    print(result)