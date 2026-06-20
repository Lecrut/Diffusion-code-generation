MIN_INT = -2147483648
MAX_INT = 2147483647

def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    if a < MIN_INT or a > MAX_INT or b < MIN_INT or b > MAX_INT:
        raise OverflowError("Input values are out of valid integer range")
    return a - b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = subtract_integers(sample_a, sample_b)
    print(result)