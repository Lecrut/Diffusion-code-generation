import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def benchmark_access():
    SIZE = 1000000
    standard_list = list(range(SIZE))
    fast_list = FastList(list(range(SIZE)))

    def time_access(lst, size):
        start_time = time.time()
        for _ in range(size):
            lst[0]
        end_time = time.time()
        return end_time - start_time
    standard_list_time = time_access(standard_list, SIZE)
    fast_list_time = time_access(fast_list, SIZE)
    return (standard_list_time, fast_list_time)
if __name__ == '__main__':
    standard_time, fast_time = benchmark_access()
    print('Standard List Access Time:', standard_time)
    print('Fast List Access Time:', fast_time)