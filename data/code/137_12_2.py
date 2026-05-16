class ConditionalTester:
    def evaluate_conditions(self, test_cases):
        for case_name, conditions in test_cases.items():
            result = True
            for condition_name, condition_value in conditions.items():
                if not condition_value:
                    result = False
                    break
            print(f"Test Case: {case_name}, Result: {'PASS' if result else 'FAIL'}")
if __name__ == '__main__':
    tester = ConditionalTester()
    sample_tests = {
        "Test A": {
            "is_positive": True,
            "is_even": False
        },
        "Test B": {
            "is_positive": True,
            "is_even": True
        },
        "Test C": {
            "is_positive": False,
            "is_even": True
        }
    }
    tester.evaluate_conditions(sample_tests)