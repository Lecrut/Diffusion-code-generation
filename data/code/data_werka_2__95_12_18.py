def check_integer_properties(n):
    if not isinstance(n, int):
        raise ValueError(f"Expected integer, got {type(n).__name__}")
    return {
        'value': n,
        'is_positive': n > 0,
        'is_even': n % 2 == 0,
        'is_less_than_100': n < 100
    }

def process_integers(a, b, c):
    return [check_integer_properties(val) for val in (a, b, c)]

if __name__ == '__main__':
    sample_values = (42, -5, 100)
    results = process_integers(*sample_values)
    print(results)