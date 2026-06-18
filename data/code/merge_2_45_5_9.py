def validate_and_compute(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    try:
        a = float(args[0])
        b = float(args[1])
        mean_val = (a + b) / 2
        sum_val = a + b
        return {
            "mean": mean_val,
            "sum": sum_val
        }
    except ValueError as e:
        raise TypeError(f"Arguments must be numeric. Error details: {e}")
if __name__ == '__main__':
    result = validate_and_compute(10, 20)
    print(result["mean"])
    print(result["sum"])