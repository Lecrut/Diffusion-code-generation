import time

class FastList:
    def __init__(self):
        self.data = {}

    def append(self, value):
        index = len(self.data)
        self.data[index] = value

    def get(self, index):
        return self.data.get(index)

def benchmark():
    size = 10**6
    fast_list = FastList()
    normal_list = []

    start_time = time.time()
    for i in range(size):
        fast_list.append(i)
    end_time = time.time()
    print(f"FastList append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(size):
        normal_list.append(i)
    end_time = time.time()
    print(f"Normal List append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(size):
        fast_list.get(i % size)
    end_time = time.time()
    print(f"FastList get: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(size):
        normal_list[i % size]
    end_time = time.time()
    print(f"Normal List get: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()