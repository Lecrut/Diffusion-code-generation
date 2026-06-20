def are_both_true(val1, val2):
    return bool(val1) and bool(val2)

if __name__ == '__main__':
    test_cases = [
        (True, True),
        (False, True),
        (True, False),
        (False, False)
    ]
    for case in test_cases:
        print(f"are_both_true({case[0]}, {case[1]}) -> {are_both_true(*case)}")