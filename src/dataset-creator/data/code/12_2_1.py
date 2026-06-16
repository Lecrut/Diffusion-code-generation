import numbers
class OddnessValidator:
    def validate_oddness(self, data_list):
        if not isinstance(data_list, list):
            return False
        for item in data_list:
            try:
                num = int(item)
                if num % 2 == 0:
                    return False
            except (ValueError, TypeError):
                return None
        return True
if __name__ == '__main__':
    test_cases = [
        [1, 3, 5],
        [-1, -3],
        [None, 1, 'a'],
        [True, False],
        [],
        [2, 4, 6],
        None,
        "not a list"
    ]
    validator = OddnessValidator()
    for i, case in enumerate(test_cases):
        result = validator.validate_oddness(case)
        print(f"Test Case {i+1}: Input={case}, Result={result}")