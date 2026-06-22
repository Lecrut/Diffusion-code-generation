import time

class FastList:
    def __init__(self, elements):
        self.elements = elements
    
    def get(self, index):
        return self.elements[index]

def benchmark_access():
    SIZE = 1000000
    STANDARD_LIST = list(range(SIZE))
    FAST_LIST = FastList(list(range(SIZE)))
    
    def time_standard_list_access(lst, size):
        start_time = time.time()
        for i in range(size):
            _ = lst[i]
        end_time = time.time()
        return end_time - start_time
    
    def time_fast_list_access(fast_lst, size):
        start_time = time.time()
        for i in range(size):
            _ = fast_lst.get(i)
        end_time = time.time()
        return end_time - start_time
    
    standard_list_time = time_standard_list_access(STANDARD_LIST, SIZE)
    fast_list_time = time_fast_list_access(FAST_LIST, SIZE)
    
    return standard_list_time, fast_list_time

if __name__ == '__main__':
    standard_time, fast_time = benchmark_access()
    print(f"Standard List Access Time: {standard_time:.6f} seconds")
    print(f"Fast List Access Time: {fast_time:.6f} seconds")