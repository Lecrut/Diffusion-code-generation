import time

class FastList:
    def __init__(self):
        self._data = {}

    def append(self, value):
        index = len(self._data)
        self._data[index] = value

    def __getitem__(self, index):
        return self._data[index]

def benchmark():
    n = 1000000
    python_list = list(range(n))
    fast_list = FastList()
    for i in range(n):
        fast_list.append(i)

    start_time = time.time()
    for _ in range(10000):
        python_list[500000]
    python_time = time.time() - start_time

    start_time = time.time()
    for _ in range(10000):
        fast_list[500000]
    fast_time = time.time() - start_time

    print(f"Python list access time: {python_time:.6f} seconds")
    print(f"FastList access time: {fast_time:.6f} seconds")

if __name__ == '__main__':
    benchmark()