def validate_inputs(a, b, c):
    checks = {
        "a": {"positive": a > 0, "even": a % 2 == 0, "magnitude": a < 100},
        "b": {"positive": b > 0, "even": b % 2 == 0, "magnitude": b < 100},
        "c": {"positive": c > 0, "even": c % 2 == 0, "magnitude": c < 100}
    }
    return checks

if __name__ == '__main__':
    inputs = [50, 42, 98]
    results = validate_inputs(*inputs)
    print(results)