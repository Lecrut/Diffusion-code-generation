def validate_and_compute(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    try:
        a = float(args[0])
        b = float(args[1])
        mean = (a + b) / 2.0
        return {"mean": mean, "sum": a + b}
    except ValueError as e:
        raise TypeError("Arguments must be numeric.") from e
if __name__ == '__main__':
    result = validate_and_compute(10, 20)
    print(f"Mean: {result['mean']}, Sum: {result['sum']}")