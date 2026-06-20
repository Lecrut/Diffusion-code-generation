from typing import Tuple

def validate_input(a: any, b: any) -> bool:
    return isinstance(a, (int, float)) and isinstance(b, (int, float))

def reverse_order(a: int, b: int) -> Tuple[int, int]:
    if not validate_input(a, b):
        raise ValueError("Inputs must be numbers")
    return (b, a)

if __name__ == '__main__':
    result = reverse_order(42, 24)
    print(result)