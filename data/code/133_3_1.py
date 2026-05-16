def check_majority(statements):
    true_count = sum(1 for s in statements if s == "True")
    return true_count > len(statements) / 2
if __name__ == '__main__':
    test_statements1 = ["True", "False", "True", "False"]
    test_statements2 = ["True", "True", "False", "False"]
    test_statements3 = ["True", "False", "False"]
    test_statements4 = ["True", "True", "True"]
    print(f"Test 1: {check_majority(test_statements1)}")
    print(f"Test 2: {check_majority(test_statements2)}")
    print(f"Test 3: {check_majority(test_statements3)}")
    print(f"Test 4: {check_majority(test_statements4)}")