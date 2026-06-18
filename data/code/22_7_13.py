def get_remainder(n: int) -> int:
    """Returns the remainder of n divided by 2."""
    return n % 2

if __name__ == '__main__':
    # Sample values to test odd/even determination without user input
    samples = [10, -3, 7, 0]

    for num in samples:
        remainder = get_remainder(num)
        if remainder == 0:
            status = "even"
        else:
            status = "odd"
        print(f"{num} is {status}")