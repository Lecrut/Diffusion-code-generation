import statistics as st
def compute_stats(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_val = st.mean([a, b, c])
    return (mean_val, total)
if __name__ == '__main__':
    x, y, z = 10.5, 20.3, 30.7
    result_mean, result_total = compute_stats(x, y, z)
    print(f"Mean: {result_mean}, Total: {result_total}")