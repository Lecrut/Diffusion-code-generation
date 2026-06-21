import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access():
    size = 1000000
    sample_list = list(range(size))
    fast_list = FastList(sample_list)
    start_time = time.time()
    for i in range(size):
        _ = sample_list[i]
    std_list_time = time.time() - start_time
    start_time = time.time()
    for i in range(size):
        _ = fast_list.get(i)
    fast_list_time = time.time() - start_time
    return (std_list_time, fast_list_time)
if __name__ == '__main__':
    std_list_time, fast_list_time = benchmark_access()
    print(f'Standard List Access Time: {std_list_time:.6f} seconds')
    print(f'FastList Access Time: {fast_list_time:.6f} seconds')