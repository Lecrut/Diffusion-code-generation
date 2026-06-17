import time
def multiply_two_amounts(a: float, b: float) -> float:
    return a * b
if __name__ == '__main__':
    amount1 = 123.456789
    amount2 = 987.654321
    start_time = time.perf_counter()
    result = multiply_two_amounts(amount1, amount2)
    end_time = time.perf_counter()
    print(f"Result: {result}")
    print(f"Execution time: {(end_time - start_time):.9f} seconds")