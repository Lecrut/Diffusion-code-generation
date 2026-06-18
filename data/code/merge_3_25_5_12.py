from typing import Union

def is_zero(x: Union[int, float]) -> bool:
    """Check if a number is numerically equivalent to zero."""
    return x == 0 or (x != int) and abs(float(int(round(x)))) < 1e-9

if __name__ == '__main__':
    test_values = [0.0, -0.0, 1, -1, 2.5, float('inf'), float('-inf')]
    for val in test_values:
        print(f"{val!r}: {is_zero(val)}")