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
    py_list = []
    fast_list = FastList()

    start_time = time.time()
    for i in range(n):
        py_list.append(i)
    end_time = time.time()
    print(f"Python list append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        fast_list.append(i)
    end_time = time.time()
    print(f"FastList append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        _ = py_list[i]
    end_time = time.time()
    print(f"Python list access: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        _ = fast_list[i]
    end_time = time.time()
    print(f"FastList access: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()