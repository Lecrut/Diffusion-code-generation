import time
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for i in range(1, len(data)):
        if data[i] < minimum:
            minimum = data[i]
    return minimum
if __name__ == '__main__':
    sample_list = [34, 12, 56, 9, 88, 45, 7]
    start_time = time.perf_counter()
    result = find_minimum(sample_list)
    end_time = time.perf_counter()
    print(result)