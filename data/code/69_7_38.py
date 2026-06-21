import time

class FastList:
    def __init__(self, elements):
        self.elements = elements
    
    @staticmethod
    def validate_index(index, length):
        if not isinstance(index, int) or index < 0 or index >= length:
            raise IndexError("Index out of range")
    
    def get(self, index):
        FastList.validate_index(index, len(self.elements))
        return self.elements[index]

def benchmark_access():
    SIZE = 1000000
    STANDARD_LIST = list(range(SIZE))
    FAST_LIST = FastList(list(range(SIZE)))
    
    def time_access(lst, size):
        start_time = time.time()
        for i in range(size):
            _ = lst[i]
        end_time = time.time()
        return end_time - start_time
    
    standard_list_time = time_access(STANDARD_LIST, SIZE)
    fast_list_time = time_access([FAST_LIST.get(i) for i in range(SIZE)], SIZE)
    
    return standard_list_time, fast_list_time

if __name__ == '__main__':
    standard_time, fast_time = benchmark_access()
    print(f"Standard list access time: {standard_time} seconds")
    print(f"Fast list access time: {fast_time} seconds")