import time

class FastAccessList:
    def __init__(self):
        self._data = {}
    
    def append(self, value):
        index = len(self._data)
        self._data[index] = value
    
    def __getitem__(self, index):
        return self._data[index]

def benchmark_access():
    n = 1000000
    python_list = list(range(n))
    fast_access_list = FastAccessList()
    for i in range(n):
        fast_access_list.append(i)
    
    start_time = time.time()
    for _ in range(1000):
        value = python_list[500000]
    end_time = time.time()
    print(f"Python list access time: {end_time - start_time} seconds")
    
    start_time = time.time()
    for _ in range(1000):
        value = fast_access_list[500000]
    end_time = time.time()
    print(f"FastAccessList access time: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark_access()