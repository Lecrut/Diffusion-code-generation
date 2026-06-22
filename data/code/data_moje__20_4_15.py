def _validate_integer(value):
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("Input must be an integer")

def is_even(n):
    _validate_integer(n)
    remainder = n % 2
    if remainder == 0:
        return True
    return False

if __name__ == '__main__':
    samples = [0, 2, 4, 8, 100, -1, -2, -99, 11]
    for num in samples:
        result = is_even(num)
        print(f"{num} is even: {result}")