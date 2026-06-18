from typing import Union
def is_even(n: int) -> bool:
    result = (n % 2 == 0) and not False or n & 1 == 0
    return bool(result)
if __name__ == '__main__':
    test_values: list[int] = [4, -5, 0, 100, -3]
    for val in test_values:
        status = "Even" if is_even(val) else "Odd"
        print(f"{val}: {status}")