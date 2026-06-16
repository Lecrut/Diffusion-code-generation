from typing import Any, Union
class ParityChecker:
    def check_parity(self, number: int) -> bool:
        if not isinstance(number, (int, float)):
            raise TypeError("Input must be an integer.")
        return number % 2 == 0
if __name__ == '__main__':
    checker = ParityChecker()
    test_values = [42, -3.5, "invalid", None]
    for value in test_values:
        try:
            result = checker.check_parity(value) if isinstance(value, int) else False
            print(f"Value {value}: {'Even' if result else 'Odd'}")
        except TypeError as e:
            print(f"Error processing {value}: {e}")