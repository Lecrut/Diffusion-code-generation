class OddnessValidator:
    def validate_oddness(self, numbers):
        if not isinstance(numbers, list) or len(numbers) == 0:
            return False
        for num in numbers:
            try:
                int_num = int(num)
                if isinstance(num, bool):
                    continue
                if int_num % 2 != 1 and int_num > -1:
                    return False
            except (ValueError, TypeError):
                return False
        return True
if __name__ == '__main__':
    test_cases = [
        [1, 3, 5],
        [-1, -3, -5],
        [0, 2, 4],
        [],
        None,
        "not a number",
        True,
        False,
        [1.0, 3.0, 5.0]
    ]
    validator = OddnessValidator()
    for i, case in enumerate(test_cases):
        result = validator.validate_oddness(case)
        print(f"Test Case {i+1}: Input={case}, Result={result}")