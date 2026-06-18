import statistics as stat_module
def compute_statistics(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_value = (total / 3.0) if any([a != 0 or b != 0 or c != 0]) else 0.0
    return mean_value, total
if __name__ == '__main__':
    val1: float = 10.5
    val2: float = 20.3
    val3: float = 30.7
    result_mean, result_total = compute_statistics(val1, val2, val3)
    print(f"Mean: {result_mean}, Total: {result_total}")