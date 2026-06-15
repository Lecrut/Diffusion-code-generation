import time
def find_sum_of_three(a, b, c):
    return a + b + c
if __name__ == '__main__':
    num1 = 10
    num2 = 25
    num3 = 5
    start_time = time.perf_counter()
    result = find_sum_of_three(num1, num2, num3)
    end_time = time.perf_counter()
    print(result)