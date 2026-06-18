from typing import Optional
def check_positive(value: float, epsilon: Optional[float] = None) -> bool:
    threshold = epsilon if epsilon is not None else 1e-9
    return value > threshold
if __name__ == '__main__':
    test_cases = [0.5, -2.3, 1e-10, 0]
    for case in test_cases:
        result = check_positive(case)
        print(f"check_positive({case}) = {result}")