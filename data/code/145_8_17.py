def evaluate_complex_predicate(predicates):
    for predicate in predicates:
        if not predicate():
            return False
    return True

if __name__ == '__main__':
    sample_values = [
        lambda: 1 > 0,
        lambda: 2 < 3,
        lambda: 4 == 4
    ]
    print(evaluate_complex_predicate(sample_values))