import time
SAMPLE_SIZE = 1000000

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access_time(data, access_function, iterations):
    start_time = time.time()
    for _ in range(iterations):
        for i in range(len(data)):
            access_function(i)
    end_time = time.time()
    return end_time - start_time
if __name__ == '__main__':
    sample_data = list(range(SAMPLE_SIZE))
    standard_list_time = benchmark_access_time(sample_data, lambda index: sample_data[index], SAMPLE_SIZE)
    fast_list = FastList(sample_data)
    fast_list_time = benchmark_access_time(fast_list.elements, fast_list.get, SAMPLE_SIZE)
    print(f'Standard Python list access time: {standard_list_time:.6f} seconds')
    print(f'Custom FastList access time: {fast_list_time:.6f} seconds')