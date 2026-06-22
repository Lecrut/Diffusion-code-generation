def is_even_bitwise(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == '__main__':
    print(is_even_bitwise(0))
    print(is_even_bitwise(1))
    print(is_even_bitwise(2))
    print(is_even_bitwise(-3))
    print(is_even_bitwise(100))