import time

class FastList:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Elements must be a list")
        self.elements = elements
    
    def get(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements[index]

def benchmark_access():
    SIZE = 1000000
    STANDARD_LIST = list(range(SIZE))
    FAST_LIST = FastList(list(range(SIZE)))
    
    def time_access(lst, size):
        start_time = time.time()
        for i in range(size):
            _ = lst[i]
        return time.time() - start_time
    
    standard_list_time = time_access(STANDARD_LIST, SIZE)
    fast_list_time = time_access([FAST_LIST.get(i) for i in range(SIZE)], SIZE)
    
    return standard_list_time, fast_list_time

if __name__ == '__main__':
    std_time, fast_time = benchmark_access()
    print(f"Standard list access time: {std_time:.6f} seconds")
    print(f"FastList access time: {fast_time:.6f} seconds")