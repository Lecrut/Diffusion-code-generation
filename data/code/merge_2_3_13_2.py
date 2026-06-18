from typing import Any, Union
class ParityChecker:
    def is_even(self, number: Any) -> bool:
        if not isinstance(number, (int, float)):
            raise TypeError(f"Invalid data type {type(number).__name__}. Expected int or float.")
        try:
            numeric_value = float(number)
            return numeric_value % 2 == 0
        except Exception as e:
            raise ValueError(f"Cannot convert number to valid numeric value for parity check: {e}")
if __name__ == '__main__':
    checker = ParityChecker()
    test_cases = [4, -10.5, "invalid", None]
    import logging
    logging.basicConfig(level=logging.INFO)
    for val in test_cases:
        try:
            result = checker.is_even(val)
            logging.info(f"Number {val} is even: {result}")
        except (TypeError, ValueError) as error:
            logging.error(f"Error processing number {val}: {error}")