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
    print(f"FastList append: {end_time - start_time:.6f} seconds")

    start_time = time.time()
    for i in range(size):
        standard_list.append(i)
    end_time = time.time()
    print(f"Standard List append: {end_time - start_time:.6f} seconds")

    fast_list_access_time = 0
    standard_list_access_time = 0

    for _ in range(1000):
        index = size // 2
        start_time = time.time()
        value = fast_list[index]
        end_time = time.time()
        fast_list_access_time += (end_time - start_time)

        start_time = time.time()
        value = standard_list[index]
        end_time = time.time()
        standard_list_access_time += (end_time - start_time)

    print(f"FastList access: {fast_list_access_time / 1000:.6f} seconds")
    print(f"Standard List access: {standard_list_access_time / 1000:.6f} seconds")

if __name__ == '__main__':
    benchmark()