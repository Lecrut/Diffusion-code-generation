def evaluate_complex_predicate(predicate):
    return predicate()

if __name__ == '__main__':
    sample_values = [
        lambda: 1 > 0,
        lambda: 2 < 3,
        lambda: 4 == 4,
        lambda: 5 != 6
    ]
    
    complex_predicate = all(sample_values)
    print(evaluate_complex_predicate(complex_predicate))