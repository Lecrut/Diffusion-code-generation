import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access():
    sample_size = 1000000
    sample_data = list(range(sample_size))
    start_time = time.time()
    for i in range(sample_size):
        _ = sample_data[i]
    standard_list_time = time.time() - start_time
    fast_list = FastList(sample_data)
    start_time = time.time()
    for i in range(sample_size):
        _ = fast_list.get(i)
    fast_list_time = time.time() - start_time
    return (standard_list_time, fast_list_time)
if __name__ == '__main__':
    standard_time, fast_time = benchmark_access()
    print(f'Standard Python list access time: {standard_time:.6f} seconds')
    print(f'FastList access time: {fast_time:.6f} seconds')