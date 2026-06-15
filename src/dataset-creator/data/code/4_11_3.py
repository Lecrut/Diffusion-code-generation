import time
def find_sum_of_three(a: float, b: float, c: float) -> float:
    return a + b + c
if __name__ == '__main__':
    num1 = 10.5
    num2 = 20.75
    num3 = 5.0
    start_time = time.perf_counter()
    result = find_sum_of_three(num1, num2, num3)
    end_time = time.perf_counter()
    print(result)