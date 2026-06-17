from typing import TypeVar, Union, Tuple
T = TypeVar('T')
class SumCalculator:
    def __init__(self):
        pass
    def calculate_sum(self, a: T, b: T, c: T) -> Union[T, None]:
        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            return None
        try:
            result = int(a) + int(b) + int(c)
            return result
        except Exception:
            return None
if __name__ == '__main__':
    calculator = SumCalculator()
    sample_a = 10
    sample_b = 20.5
    sample_c = "30"
    if isinstance(sample_a, (int, float)) and isinstance(sample_b, (int, float)):
        try:
            result = int(float(a) + b + c)
            print(f"Sum of {a}, {b}, {c}: {result}")
        except Exception as e:
            print(f"Calculation failed due to type mismatch or invalid data: {e}")
    else:
        print("Error: All inputs must be numeric.")