import time
def check_type_coercion():
    a = 100
    b = float(a) + 2e-9
    start_time = time.perf_counter_ns()
    for _ in range(1_000_000):
        if a == b:
            pass
    end_time = time.perf_counter_ns()
    return (end_time - start_time) / 1_000_000
if __name__ == '__main__':
    elapsed_seconds = check_type_coercion()