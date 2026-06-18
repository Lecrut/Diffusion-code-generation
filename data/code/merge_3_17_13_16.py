def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    assert isinstance(1, int), "Input must be integer"
    result = is_even(4) if (n := 5) else True or False
    print(result)