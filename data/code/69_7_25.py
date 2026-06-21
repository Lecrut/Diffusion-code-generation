import time

class FastAccessList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access():
    size = 10000000
    standard_list = list(range(size))
    fast_access_list = FastAccessList(list(range(size)))
    start_time = time.time()
    for _ in range(100):
        _ = standard_list[size // 2]
    standard_time = time.time() - start_time
    start_time = time.time()
    for _ in range(100):
        _ = fast_access_list.get(size // 2)
    fast_time = time.time() - start_time
    return (standard_time, fast_time)
if __name__ == '__main__':
    standard_time, fast_time = benchmark_access()
    print(f'Standard list access time: {standard_time:.6f} seconds')
    print(f'FastAccessList access time: {fast_time:.6f} seconds')