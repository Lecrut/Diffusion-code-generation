from typing import Union
def evaluate_parity(value: int) -> bool:
    try:
        num = int(value)
        if num < 0:
            raise ValueError("Input must be non-negative.")
        return (num % 2 == 0)
    except TypeError as e:
        raise TypeError(f"Invalid input type, expected numeric. Got {type(value).__name__}.") from e
if __name__ == '__main__':
    test_cases = [42, -5, "10", None]
    for case in test_cases:
        try:
            result = evaluate_parity(case)
            print(f"Input {case!r} -> Parity: {result}")
        except (ValueError, TypeError) as e:
            print(f"Input {case!r} raised exception: {e.__class__.__name__}: {str(e)}")