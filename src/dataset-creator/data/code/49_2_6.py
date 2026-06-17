class NumericValidator:
    def has_positive_result(self, results):
        return any(r > 0 for r in results)
if __name__ == '__main__':
    validator = NumericValidator()
    test_cases = [
        [-1.5, -2.3],
        [0, 1.1],
        [-5.6789, 4.2],
        [],
        [float('inf'), float('-inf')]
    ]
    for i, case in enumerate(test_cases):
        result = validator.has_positive_result(case)
        print(f"Case {i}: {case} -> Positive exists: {result}")