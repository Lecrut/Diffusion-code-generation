def check_majority(statements):
    true_count = sum(1 for s in statements if s == "True")
    return true_count > len(statements) / 2
if __name__ == '__main__':
    test_statements_1 = ["True", "False", "True", "True"]
    print(check_majority(test_statements_1))
    test_statements_2 = ["False", "False", "True", "False"]
    print(check_majority(test_statements_2))
    test_statements_3 = ["True", "False", "False"]
    print(check_majority(test_statements_3))