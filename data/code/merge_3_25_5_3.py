from typing import Union
import math

def is_zero(value: Union[int, float]) -> bool:
    return abs(value) < 1e-9 if isinstance(value, (int, float)) else False

if __name__ == '__main__':
    test_values = [0, -0.5, 3.141592653589793, math.sqrt(2), int(float('nan')), -0]
    for val in test_values:
        print(f"{val!r}: {is_zero(val)}")