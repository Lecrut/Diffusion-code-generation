class ConditionalTester:
    def evaluate_conditions(self, test_cases):
        for case_id, conditions in test_cases.items():
            result = True
            for condition_name, condition_value in conditions.items():
                if not eval(f"{condition_value}"):
                    result = False
                    break
            print(f"Test Case {case_id}: {'PASS' if result else 'FAIL'}")
if __name__ == '__main__':
    tester = ConditionalTester()
    sample_tests = {
        1: {
            "A > 5": True,
            "B == 10": False
        },
        2: {
            "C < 20": True,
            "D == 5": True
        },
        3: {
            "E > 100": False,
            "F == 50": True
        }
    }
    tester.evaluate_conditions(sample_tests)