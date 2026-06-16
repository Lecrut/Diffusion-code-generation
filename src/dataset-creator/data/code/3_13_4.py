from typing import Union
class ParityChecker:
    def is_even(self, number: Union[int, float]) -> bool:
        if not isinstance(number, (int, float)):
            raise TypeError("Input must be an integer or a floating-point number.")
        try:
            int_value = int(float(number))
            return int_value % 2 == 0
        except ValueError as e:
            raise ValueError(f"Invalid numeric value provided: {e}")
if __name__ == '__main__':
    checker = ParityChecker()
    test_cases = [4, -3.5, "10", None]
    for case in test_cases:
        try:
            result = checker.is_even(case)
            print(f"Input {case} is even: {result}")
        except (TypeError, ValueError) as error:
            print(f"Error processing input {case}: {error}")