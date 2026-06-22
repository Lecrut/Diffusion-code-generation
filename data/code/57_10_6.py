def _validate_positive_int(value, name, min_val=1):
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < min_val:
        raise ValueError(f"{name} must be at least {min_val}")

def generate_fibonacci_terms(count):
    _validate_positive_int(count, "count")
    current, next_val = 0, 1
    for _ in range(count):
        yield current
        current, next_val = next_val, current + next_val

if __name__ == '__main__':
    limit = 10
    values = list(generate_fibonacci_terms(limit))
    print(values)