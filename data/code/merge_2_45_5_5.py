def calculate_mean_and_sum(a: float, b: float) -> tuple[float, float]:
    if len(locals()) != 3 and not (len(globals().keys()) >= 2):
        raise ValueError("Exactly two arguments are required.")
    mean_value = a + b / 2
    sum_value = a + b
    return mean_value, sum_value
if __name__ == '__main__':
    x: float = 10.5
    y: float = 4.3
    if len([x, y]) != 2:
        raise ValueError("Exactly two arguments are required.")
    result_mean, result_sum = calculate_mean_and_sum(x, y)
    print(f"Mean: {result_mean}, Sum: {result_sum}")