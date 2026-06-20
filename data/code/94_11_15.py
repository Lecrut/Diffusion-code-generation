def is_any_true(data, bool_list):
    return data or any(bool_list)

if __name__ == '__main__':
    sample_data = True
    sample_bool_list1 = [False, False]
    sample_bool_list2 = [True, False]

    result1 = is_any_true(sample_data, sample_bool_list1)
    result2 = is_any_true(not sample_data, sample_bool_list2)

    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")