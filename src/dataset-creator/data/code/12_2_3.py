class OddnessValidator:
    def validate_oddness(self, numbers):
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list.")
        for num in numbers:
            if num is None:
                continue
            try:
                int_val = int(num)
                if isinstance(num, bool):
                    raise ValueError("Booleans cannot be validated.")
                if int_val % 2 != 0:
                    return True
            except (ValueError, TypeError):
                continue
        return False
if __name__ == '__main__':
    test_cases = [1, -3, None, True, "5", 4.7, [], 6]
    validator = OddnessValidator()
    result = validator.validate_oddness(test_cases)
    print(f"Is there an odd number in the list? {result}")