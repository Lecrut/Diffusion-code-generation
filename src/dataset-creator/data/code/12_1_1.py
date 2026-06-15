import time
def add_numbers(a: int, b: int) -> int:
    return a + b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    start_time = time.perf_counter()
    result = add_numbers(num1, num2)
    end_time = time.perf_counter()
    print(f"Result: {result}")
    print(f"Execution time: {(end_time - start_time) * 1e6:.3f} microseconds")