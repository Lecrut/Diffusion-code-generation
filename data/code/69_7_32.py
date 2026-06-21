import time

class FastList:
    DEFAULT_SIZE = 1000000
    
    def __init__(self, elements):
        self.elements = elements
    
    @staticmethod
    def get_element(elements, index):
        return elements[index]
    
    def access_time(self, size):
        start_time = time.time()
        for i in range(size):
            _ = FastList.get_element(self.elements, i)
        end_time = time.time()
        return end_time - start_time

def benchmark_access():
    standard_list = list(range(FastList.DEFAULT_SIZE))
    fast_list = FastList(list(range(FastList.DEFAULT_SIZE)))
    
    standard_list_start_time = time.time()
    for i in range(FastList.DEFAULT_SIZE):
        _ = standard_list[i]
    standard_list_end_time = time.time()
    standard_list_access_time = standard_list_end_time - standard_list_start_time
    
    fast_list_access_time = fast_list.access_time(FastList.DEFAULT_SIZE)
    
    return standard_list_access_time, fast_list_access_time

if __name__ == '__main__':
    std_time, fast_time = benchmark_access()
    print(f"Standard list access time: {std_time} seconds")
    print(f"Fast list access time: {fast_time} seconds")