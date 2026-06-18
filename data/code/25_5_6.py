from typing import Union

def is_zero(x: Union[int, float]) -> bool:
    return x == 0 if isinstance(x, (int, float)) else False

if __name__ == '__main__':
    test_cases = [0.0, -0.0, 1e-9, int(3), 2 / 7]
    for val in test_cases:
        print(f"{val!r}: {is_zero(val)}")