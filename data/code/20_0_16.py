def _is_non_negative_integer(val):
    return isinstance(val, int) and val >= 0

def is_even(n: int) -> bool:
    if not _is_non_negative_integer(n):
        return False
    remainder = n % 2
    return remainder == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-3))
    print(is_even(12))