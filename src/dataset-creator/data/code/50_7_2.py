import statistics as stats
def compute_mean_and_total(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_val = (a + b + c) / 3
    return mean_val, total
if __name__ == '__main__':
    val1 = 10.5
    val2 = 20.7
    val3 = 30.9
    result_mean, result_total = compute_mean_and_total(val1, val2, val3)
    print(f"Mean: {result_mean}, Total: {result_total}")