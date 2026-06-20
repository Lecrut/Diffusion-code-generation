MIN_INT = -2147483648
MAX_INT = 2147483647

def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    result = a - b
    if result < MIN_INT or result > MAX_INT:
        raise OverflowError("Result is out of 32-bit signed integer range")
    return result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = subtract_integers(sample_a, sample_b)
    print(result)