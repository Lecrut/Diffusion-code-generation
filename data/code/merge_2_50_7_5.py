import statistics as st
def compute_mean_and_total(a: float, b: float, c: float) -> tuple[float, float]:
    total = a + b + c
    mean_val = st.mean([a, b, c])
    return (mean_val, total)
if __name__ == '__main__':
    val1 = 10.5
    val2 = 20.3
    val3 = 30.7
    result_mean, result_total = compute_mean_and_total(val1, val2, val3)
    print(f"Mean: {result_mean}, Total: {result_total}")