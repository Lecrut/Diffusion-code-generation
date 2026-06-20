import time

class FastIndexList:
    def __init__(self):
        self._data = {}
    
    def append(self, value):
        index = len(self._data)
        self._data[index] = value
    
    def __getitem__(self, index):
        return self._data[index]

def benchmark_access():
    n = 1000000
    standard_list = list(range(n))
    fast_index_list = FastIndexList()
    
    for i in range(n):
        fast_index_list.append(i)
    
    start_time = time.time()
    for _ in range(n):
        _ = standard_list[500000]
    end_time = time.time()
    print(f"Standard list access time: {end_time - start_time} seconds")
    
    start_time = time.time()
    for _ in range(n):
        _ = fast_index_list[500000]
    end_time = time.time()
    print(f"FastIndexList access time: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark_access()