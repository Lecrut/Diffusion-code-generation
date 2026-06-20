def check_any_true(bool_list):
    for item in bool_list:
        if item:
            return True
    return False

if __name__ == '__main__':
    sample1 = [False, False, True]
    sample2 = [False, False, False]
    sample3 = []
    sample4 = [True, True, True]
    print(f"Sample 1: {sample1} -> Result: {check_any_true(sample1)}")
    print(f"Sample 2: {sample2} -> Result: {check_any_true(sample2)}")
    print(f"Sample 3: {sample3} -> Result: {check_any_true(sample3)}")
    print(f"Sample 4: {sample4} -> Result: {check_any_true(sample4)}")