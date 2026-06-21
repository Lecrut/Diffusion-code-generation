import time

class FastList:
    def __init__(self, elements):
        self.elements = elements
    
    def get(self, index):
        return self.elements[index]

def benchmark_access_time(data_structure, size):
    sample_data = list(range(size))
    start_time = time.time()
    for i in range(size):
        _ = data_structure.get(i)
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    sample_size = 1000000
    standard_list = list(range(sample_size))
    fast_list = FastList(standard_list)
    
    standard_access_time = benchmark_access_time(fast_list, sample_size)
    print(f'Standard Python list access time: {standard_access_time:.6f} seconds')