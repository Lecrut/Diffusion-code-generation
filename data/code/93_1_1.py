def are_both_false(a, b):
    return not a and not b
if __name__ == '__main__':
    print(f"are_both_false(False, False): {are_both_false(False, False)}")
    print(f"are_both_false(False, True): {are_both_false(False, True)}")
    print(f"are_both_false(True, False): {are_both_false(True, False)}")
    print(f"are_both_false(True, True): {are_both_false(True, True)}")