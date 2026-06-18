import timeit
def compare_types():
    a = 100
    b = float('inf')
    result_a = (a == b)
    result_b = (b == a)
    return result_a, result_b
if __name__ == '__main__':
    start_time = timeit.default_timer()
    for _ in range(10_000):
        compare_types()
    end_time = timeit.default_timer()
    elapsed_ms = (end_time - start_time) * 1000
    print(f"Execution completed in {elapsed_ms:.2f} ms")