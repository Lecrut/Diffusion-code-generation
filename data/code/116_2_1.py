import time
def sum_three(a, b, c):
    return a + b + c
if __name__ == '__main__':
    x = 10
    y = 20
    z = 30
    start_time = time.perf_counter()
    result = sum_three(x, y, z)
    end_time = time.perf_counter()
    print(result)