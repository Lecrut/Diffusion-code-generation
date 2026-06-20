def is_any_true(data, bool_list):
    return data or any(bool_list)

if __name__ == '__main__':
    sample1 = (True, [False, False])
    sample2 = (False, [True, False])
    sample3 = (False, [False, True])
    sample4 = (False, [])

    print(f"Sample 1: {is_any_true(*sample1)}")
    print(f"Sample 2: {is_any_true(*sample2)}")
    print(f"Sample 3: {is_any_true(*sample3)}")
    print(f"Sample 4: {is_any_true(*sample4)}")