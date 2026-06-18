def compute_stats(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_val = total / 3
    return mean_val, total
if __name__ == '__main__':
    result_mean, result_total = compute_stats(10.5, 20.0, 30.5)
    print(f"Mean: {result_mean}, Total: {result_total}")