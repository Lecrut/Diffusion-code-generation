import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access_times(size):
    sample_data = list(range(size))
    start_time = time.time()
    for i in range(size):
        _ = sample_data[i]
    standard_list_time = time.time() - start_time
    fast_list = FastList(sample_data)
    start_time = time.time()
    for i in range(size):
        _ = fast_list.get(i)
    fast_list_time = time.time() - start_time
    return (standard_list_time, fast_list_time)
if __name__ == '__main__':
    size = 1000000
    std_time, fast_time = benchmark_access_times(size)
    print(f'Standard Python list access time: {std_time:.6f} seconds')
    print(f'FastList access time: {fast_time:.6f} seconds')