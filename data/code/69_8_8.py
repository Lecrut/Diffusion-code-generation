import time

class FastIndexList:
    def __init__(self):
        self.data = {}

    @staticmethod
    def from_list(normal_list):
        fast_list = FastIndexList()
        for index, value in enumerate(normal_list):
            fast_list.add(index, value)
        return fast_list

    def add(self, index, value):
        if index in self.data:
            raise ValueError('Index already exists')
        self.data[index] = value

    def get(self, index):
        return self.data.get(index, None)

def benchmark():
    size = 100000
    normal_list = list(range(size))
    fast_list = FastIndexList.from_list(normal_list)
    
    start_time = time.time()
    for _ in range(1000):
        value = normal_list[30000]
    end_time = time.time()
    print(f"Normal List Access: {end_time - start_time} seconds")

    start_time = time.time()
    for _ in range(1000):
        value = fast_list.get(30000)
    end_time = time.time()
    print(f"Fast Index List Access: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()