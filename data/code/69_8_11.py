import time

class FastAccessList:

    def __init__(self):
        self.data = {}

    def add(self, index, value):
        if index in self.data:
            raise ValueError('Index already exists')
        self.data[index] = value

    def get(self, index):
        return self.data.get(index, None)

def benchmark():
    size = 100000
    fast_list = FastAccessList()
    normal_list = []
    for i in range(size):
        fast_list.add(i, i)
        normal_list.append(i)
    start_time = time.time()
    for _ in range(size):
        fast_list.get(50000)
    end_time = time.time()
    print(f'FastAccessList get: {end_time - start_time} seconds')
    start_time = time.time()
    for _ in range(size):
        normal_list[50000]
    end_time = time.time()
    print(f'Normal list get: {end_time - start_time} seconds')
if __name__ == '__main__':
    benchmark()