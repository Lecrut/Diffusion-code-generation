def get_remainder(n: int) -> int:
    """Returns the remainder when integer n is divided by 2."""
    return n % 2

if __name__ == '__main__':
    # Hard-coded sample values to test odd/even determination without user input
    samples = [10, 7, -3, 0]

    for num in samples:
        remainder = get_remainder(num)
        if remainder == 1:
            status = "odd"
        else:
            status = "even"
        print(f"{num} is {status}")