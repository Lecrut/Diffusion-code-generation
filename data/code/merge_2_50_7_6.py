import statistics
def compute_stats(a: float, b: float, c: float) -> tuple[float, int]:
    return (statistics.mean([a, b, c]), a + b + c)
if __name__ == '__main__':
    result = compute_stats(10.5, 20.3, 30.7)
    print(f"Mean: {result[0]}, Total: {int(result[1])}")