class ConditionalTester:
    def evaluate_conditions(self, test_cases):
        for case in test_cases:
            result = False
            if case.get('condition_a', False) and case.get('condition_b', False):
                result = True
            print(f"Test Case: {case.get('name', 'Unnamed')}, Result: {result}")
if __name__ == '__main__':
    tester = ConditionalTester()
    sample_tests = [
        {'name': 'Test 1', 'condition_a': True, 'condition_b': True},
        {'name': 'Test 2', 'condition_a': True, 'condition_b': False},
        {'name': 'Test 3', 'condition_a': False, 'condition_b': True},
        {'name': 'Test 4', 'condition_a': False, 'condition_b': False},
        {'name': 'Test 5', 'condition_a': True, 'condition_b': True}
    ]
    tester.evaluate_conditions(sample_tests)