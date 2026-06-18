def is_divisible(a: int, b: int) -> bool:
    """Check if integer a is divisible by non-zero integer b."""
    return b != 0 and (a % b == 0)

if __name__ == '__main__':
    sample_a = 12
    sample_b = 3
    result = is_divisible(sample_a, sample_b)
    print('True' if result else 'False')