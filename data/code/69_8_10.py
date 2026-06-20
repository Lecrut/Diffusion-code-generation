import time

class FastIndexAccess:
    def __init__(self):
        self.data = {}
    
    def set(self, index, value):
        self.data[index] = value
    
    def get(self, index):
        return self.data.get(index, None)

def benchmark():
    size = 100000
    fast_access = FastIndexAccess()
    normal_list = [None] * size
    
    start_time = time.time()
    for i in range(size):
        fast_access.set(i, i)
    end_time = time.time()
    print(f"FastIndexAccess set: {end_time - start_time} seconds")
    
    start_time = time.time()
    normal_list = [i for i in range(size)]
    end_time = time.time()
    print(f"Python list append: {end_time - start_time} seconds")

if __name__ == '__main__':
    benchmark()