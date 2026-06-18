import statistics as stats
def compute_statistics(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_val = sum([a, b, c]) / 3
    return (mean_val, total)
if __name__ == '__main__':
    result_mean, result_total = compute_statistics(10.5, 20.75, 30.25)
    print(f"Mean: {result_mean}, Total: {result_total}")