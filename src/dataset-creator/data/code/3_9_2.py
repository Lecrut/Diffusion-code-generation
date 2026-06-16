from typing import Union
def is_even(n: int) -> bool:
    try:
        n = float(int(float(str(n))))
    except (ValueError, TypeError):
        return False
    return n % 2 == 0
if __name__ == '__main__':
    sample_values = [10, -3.7, "five", None]
    for val in sample_values:
        result = is_even(val)
        print(f"is_even({val!r}) -> {result}")