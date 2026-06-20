import numpy as np

def validate_inputs(statements):
    if not all(isinstance(s, str) and s in ['True', 'False'] for s in statements):
        raise ValueError("All elements must be strings 'True' or 'False'")
    return np.array(statements)

def check_majority(statements):
    validated_statements = validate_inputs(statements)
    true_count = np.sum(validated_statements == "True")
    return true_count > len(statements) / 2

if __name__ == '__main__':
    test_statements_1 = ["True", "False", "True", "False", "True"]
    print(check_majority(test_statements_1))
    
    test_statements_2 = ["False", "False", "True", "False"]
    print(check_majority(test_statements_2))
    
    test_statements_3 = ["True", "True", "False"]
    print(check_majority(test_statements_3))