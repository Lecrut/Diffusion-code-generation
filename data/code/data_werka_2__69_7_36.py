import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access():
    size = 10000000
    standard_list = list(range(size))
    fast_list = FastList(list(range(size)))
    start_time = time.time()
    for i in range(1000):
        _ = standard_list[i]
    standard_list_access_time = time.time() - start_time
    start_time = time.time()
    for i in range(1000):
        _ = fast_list.get(i)
    fast_list_access_time = time.time() - start_time
    return (standard_list_access_time, fast_list_access_time)
if __name__ == '__main__':
    std_time, fast_time = benchmark_access()
    print(f'Standard List Access Time: {std_time:.6f} seconds')
    print(f'FastList Access Time: {fast_time:.6f} seconds')