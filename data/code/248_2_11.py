def add_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    return a + b

if __name__ == '__main__':
    try:
        sample_a = 15
        sample_b = 20
        result = add_integers(sample_a, sample_b)
        print(result)
    except ValueError as e:
        print(e)