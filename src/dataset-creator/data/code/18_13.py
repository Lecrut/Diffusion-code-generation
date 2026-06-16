import time
def reverse_array(arr):
    return arr[::-1]
if __name__ == '__main__':
    data = [3, 6, 9, 2, 5, 8, 1]
    start_time = time.perf_counter()
    result = reverse_array(data)
    end_time = time.perf_counter()
    print(result)