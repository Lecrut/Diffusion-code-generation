import numpy as np

TRUE_VALUE = "True"
THRESHOLD = 0.5

def check_majority(statements):
    true_mask = np.array([s == TRUE_VALUE for s in statements])
    true_count = np.sum(true_mask)
    return true_count > len(statements) * THRESHOLD

if __name__ == '__main__':
    test_statements_1 = ["True", "False", "True", "False"]
    result_1 = check_majority(test_statements_1)
    print(f"Test 1: {result_1}")
    
    test_statements_2 = ["True", "True", "False", "False"]
    result_2 = check_majority(test_statements_2)
    print(f"Test 2: {result_2}")
    
    test_statements_3 = ["True", "False", "False"]
    result_3 = check_majority(test_statements_3)
    print(f"Test 3: {result_3}")