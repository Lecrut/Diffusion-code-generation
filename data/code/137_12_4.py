class ConditionalTester:
    def evaluate_conditions(self, test_cases):
        for case_id, conditions in test_cases.items():
            result = False
            for condition_name, condition_value in conditions.items():
                if condition_value:
                    result = True
                    break
            print(f"Test Case {case_id}: Result is {result}")
if __name__ == '__main__':
    tester = ConditionalTester()
    sample_tests = {
        1: {"is_positive": True, "is_even": False},
        2: {"is_positive": False, "is_even": True},
        3: {"is_positive": True, "is_even": True},
        4: {"is_positive": False, "is_even": False}
    }
    tester.evaluate_conditions(sample_tests)