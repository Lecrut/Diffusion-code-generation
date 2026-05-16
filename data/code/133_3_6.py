def check_majority(statements):
    true_count = sum(1 for s in statements if s == "True")
    return true_count > len(statements) / 2
if __name__ == '__main__':
    test_statements1 = ["True", "False", "True", "True"]
    test_statements2 = ["False", "False", "True", "False"]
    test_statements3 = ["True", "False", "False"]
    print(check_majority(test_statements1))
    print(check_majority(test_statements2))
    print(check_majority(test_statements3))