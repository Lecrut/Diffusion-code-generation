import time

class FastList:
    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access():
    size = 1000000
    standard_list = list(range(size))
    fast_list = FastList(list(range(size)))

    start_time = time.time()
    for i in range(size):
        _ = standard_list[i]
    standard_list_time = time.time() - start_time

    start_time = time.time()
    for i in range(size):
        _ = fast_list.get(i)
    fast_list_time = time.time() - start_time

    return standard_list_time, fast_list_time

if __name__ == '__main__':
    std_time, fast_time = benchmark_access()
    print(f"Standard List Access Time: {std_time} seconds")
    print(f"Fast List Access Time: {fast_time} seconds")