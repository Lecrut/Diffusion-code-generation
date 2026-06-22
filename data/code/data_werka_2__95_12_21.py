THRESHOLD = 100
def analyze_integer(value):
    checks = {
        'is_positive': value > 0,
        'is_even': value % 2 == 0,
        'is_less_than_100': value < THRESHOLD
    }
    return checks
def process_values(a, b, c):
    results = []
    for val in [a, b, c]:
        if not isinstance(val, int):
            raise ValueError(f"Expected integer, got {type(val).__name__}")
        results.append(analyze_integer(val))
    return results
if __name__ == '__main__':
    inputs = [99, 100, -5]
    output = process_values(*inputs)
    print(output)