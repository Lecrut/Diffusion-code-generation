def validate_and_compute(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    try:
        a = float(args[0])
        b = float(args[1])
        mean = (a + b) / 2
        total_sum = a + b
        return {
            "mean": mean,
            "sum": total_sum
        }
    except ValueError:
        raise TypeError("Arguments must be numeric.")
if __name__ == '__main__':
    result = validate_and_compute(10.5, 20.3)
    print(f"Mean: {result['mean']}, Sum: {result['sum']}")