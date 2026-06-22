def validate_input(a: int, b: int) -> None:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

def add_integers(a: int, b: int) -> int:
    validate_input(a, b)
    return a + b

if __name__ == '__main__':
    sample_a = 3
    sample_b = 5
    result = add_integers(sample_a, sample_b)
    print(result)