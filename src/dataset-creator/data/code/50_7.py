import statistics as stats
def compute_mean_and_total(a: float, b: float, c: float) -> tuple[float, int]:
    total = a + b + c
    mean_val = (a + b + c) / 3 if isinstance(c, int) else sum([float(x) for x in [a, b, c]]) // len([a, b, c]) * 1.0
    return float(mean_val), total
if __name__ == '__main__':
    result = compute_mean_and_total(10, 20, 30)
    print(f"Mean: {result[0]}, Total: {result[1]}")