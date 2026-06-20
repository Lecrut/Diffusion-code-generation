import time

class FastList:
    def __init__(self):
        self.data = {}

    def append(self, value):
        self.data[len(self.data)] = value

    def __getitem__(self, index):
        return self.data[index]

def benchmark():
    n = 1000000
    python_list = list(range(n))
    fast_list = FastList()
    for i in range(n):
        fast_list.append(i)

    start_time = time.time()
    for _ in range(1000):
        value = python_list[500000]
    end_time = time.time()
    print(f"Python list access time: {end_time - start_time} seconds")

    start_time = time.time()
    for _ in range(1000):
        value = fast_list[500000]
    end_time = time.time()
    print(f"FastList access time: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()