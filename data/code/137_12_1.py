class ConditionalTester:
    def evaluate_conditions(self, test_cases):
        for i, case in enumerate(test_cases):
            result = False
            if case.get('condition_a', False) and case.get('condition_b', False):
                result = True
            print(f"Test Case {i+1}: Result is {result}")
if __name__ == '__main__':
    tester = ConditionalTester()
    sample_tests = [
        {'condition_a': True, 'condition_b': True},
        {'condition_a': True, 'condition_b': False},
        {'condition_a': False, 'condition_b': True},
        {'condition_a': False, 'condition_b': False},
        {'condition_a': True, 'condition_b': True}
    ]
    tester.evaluate_conditions(sample_tests)