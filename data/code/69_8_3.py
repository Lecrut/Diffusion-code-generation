import time

class FastList:
    def __init__(self):
        self.data = {}

    def append(self, item):
        index = len(self.data)
        self.data[index] = item

    def __getitem__(self, index):
        return self.data[index]

def benchmark():
    n = 1000000
    python_list = []
    fast_list = FastList()

    start_time = time.time()
    for i in range(n):
        python_list.append(i)
    end_time = time.time()
    print(f"Python list append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        fast_list.append(i)
    end_time = time.time()
    print(f"FastList append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        _ = python_list[i]
    end_time = time.time()
    print(f"Python list access: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(n):
        _ = fast_list[i]
    end_time = time.time()
    print(f"FastList access: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()