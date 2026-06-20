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
    n = 100000
    fast_list = FastList()
    standard_list = []

    start_time = time.time()
    for i in range(n):
        fast_list.append(i)
    end_time = time.time()
    print(f"FastList append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        standard_list.append(i)
    end_time = time.time()
    print(f"Standard List append: {end_time - start_time} seconds")

    start_time = time.time()
    for _ in range(n):
        fast_list[0]
    end_time = time.time()
    print(f"FastList index access: {end_time - start_time} seconds")

    start_time = time.time()
    for _ in range(n):
        standard_list[0]
    end_time = time.time()
    print(f"Standard List index access: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()