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
        fast_list.get(42)
    end_time = time.time()
    print(f'Custom data structure access time: {end_time - start_time:.6f} seconds')
    start_time = time.time()
    for _ in range(size):
        normal_list[42]
    end_time = time.time()
    print(f'Standard list access time: {end_time - start_time:.6f} seconds')
if __name__ == '__main__':
    benchmark()