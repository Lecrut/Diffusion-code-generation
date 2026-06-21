def safe_tuple_get(t, index):
    if 0 <= index < len(t):
        return t[index]
    return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    valid_index = 2
    invalid_index = 10
    result_valid = safe_tuple_get(sample_tuple, valid_index)
    result_invalid = safe_tuple_get(sample_tuple, invalid_index)
    print(result_valid)
    print(result_invalid)