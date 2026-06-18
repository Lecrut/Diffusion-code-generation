from typing import Any
class SafeSummation:
    def calculate_sum(self, a: int | float, b: int | float, c: int | float) -> int | float:
        try:
            return a + b + c
        except (TypeError, ValueError):
            raise TypeError("All arguments must be numeric.")
if __name__ == '__main__':
    calculator = SafeSummation()
    result = calculator.calculate_sum(10, 20.5, -3)
    print(result)