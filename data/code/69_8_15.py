import time

class FastList:
    def __init__(self):
        self.data = {}

    def append(self, value):
        index = len(self.data)
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

def benchmark():
    size = 1000000
    fast_list = FastList()
    standard_list = []

    start_time = time.time()
    for i in range(size):
        fast_list.append(i)
    end_time = time.time()
    print(f"FastList append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(size):
        standard_list.append(i)
    end_time = time.time()
    print(f"Standard List append: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(size):
        fast_list[i]
    end_time = time.time()
    print(f"FastList access: {end_time - start_time} seconds")

    start_time = time.time()
    for i in range(size):
        standard_list[i]
    end_time = time.time()
    print(f"Standard List access: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()