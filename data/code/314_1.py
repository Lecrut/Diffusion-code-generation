import time
def calculate_total(numbers):
    return sum(numbers)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2, 8]
    start_time = time.perf_counter()
    result = calculate_total(sample_list)
    end_time = time.perf_counter()
    print(result)