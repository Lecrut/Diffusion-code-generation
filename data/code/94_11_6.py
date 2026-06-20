def is_any_true(data, bool_list):
    return data or any(bool_list)

if __name__ == '__main__':
    sample1 = is_any_true(True, [False, False])
    sample2 = is_any_true(False, [True, True])
    sample3 = is_any_true(False, [False, False])
    sample4 = is_any_true(True, [])

    print(f"Sample 1: {sample1}")
    print(f"Sample 2: {sample2}")
    print(f"Sample 3: {sample3}")
    print(f"Sample 4: {sample4}")