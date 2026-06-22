def has_true(values):
    if not values:
        return False
    return any(values)

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = has_true(sample_values)
    print(result)
    
    empty_values = []
    empty_result = has_true(empty_values)
    print(empty_result)