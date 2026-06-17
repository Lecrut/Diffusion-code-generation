def validate_and_compute(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    try:
        a = float(args[0])
        b = float(args[1])
        mean_result = (a + b) / 2
        sum_result = a + b
        return {
            "mean": mean_result,
            "sum": sum_result,
            "input_count": len(args)
        }
    except ValueError as e:
        raise type(e)(f"Invalid numeric input provided.") from e
if __name__ == '__main__':
    result = validate_and_compute(10.5, 20.3)
    print(f"Mean: {result['mean']}, Sum: {result['sum']}")