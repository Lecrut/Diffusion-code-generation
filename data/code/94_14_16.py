class TruthChecker:
    @staticmethod
    def is_any_true(input_bool, bool_list):
        return input_bool or any(bool_list)

if __name__ == '__main__':
    test_cases = [
        (True, [False, False]),
        (False, [False, False]),
        (False, [True, False]),
        (True, [True, True]),
        (False, [])
    ]
    
    for i, (input_bool, bool_list) in enumerate(test_cases):
        result = TruthChecker.is_any_true(input_bool, bool_list)
        print(f"Test Case {i+1}: {result}")