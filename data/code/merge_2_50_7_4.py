import statistics
def compute_mean_and_total(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_value = sum([a, b, c]) / 3
    return (mean_value, total)
if __name__ == '__main__':
    result_mean, result_total = compute_mean_and_total(10.5, 20.0, 30.75)
    print(f"Mean: {result_mean}, Total: {result_total}")