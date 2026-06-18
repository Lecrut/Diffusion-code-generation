def validate_and_compute(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments are required.")
    try:
        num1 = float(args[0])
        num2 = float(args[1])
        mean = (num1 + num2) / 2
        return {"mean": mean, "sum": num1 + num2}
    except ValueError as e:
        raise TypeError(f"Arguments must be numeric. Error: {e}")
if __name__ == '__main__':
    result = validate_and_compute(10, 20)
    print(result)