def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return (number & 1) == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))