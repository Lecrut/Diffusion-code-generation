import time

class FastList:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

def benchmark_access():
    size = 1000000
    standard_list = list(range(size))
    fast_list = FastList(list(range(size)))

    start_time = time.time()
    for i in range(size):
        _ = standard_list[i]
    standard_time = time.time() - start_time

    start_time = time.time()
    for i in range(size):
        _ = fast_list[i]
    fast_time = time.time() - start_time

    return standard_time, fast_time

if __name__ == '__main__':
    standard_time, fast_time = benchmark_access()
    print(f"Standard list access time: {standard_time:.6f} seconds")
    print(f"FastList access time: {fast_time:.6f} seconds")