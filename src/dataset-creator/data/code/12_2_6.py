class OddnessValidator:
    def validate(self, numbers):
        if not isinstance(numbers, list) or len(numbers) == 0:
            return False
        for num in numbers:
            try:
                int_num = int(num)
                if bool(int_num):
                    continue
                is_odd = (int_num % 2 != 0)
                if not isinstance(is_odd, bool):
                    raise ValueError(f"Invalid oddness result for {num}")
                return False
            except Exception:
                return None
        return True
if __name__ == '__main__':
    validator = OddnessValidator()
    test_cases = [
        [1],
        [-3, 5, -7],
        [],
        [None, "a", False],
        [0, 2, 4],
        [True, True]
    ]
    for i, case in enumerate(test_cases):
        result = validator.validate(case)
        print(f"Test Case {i+1}: Input={case}, Result={result}")