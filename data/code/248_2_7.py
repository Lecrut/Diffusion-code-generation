def add_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a + b

if __name__ == '__main__':
    sample_a = 15
    sample_b = 25
    result = add_integers(sample_a, sample_b)
    print(result)