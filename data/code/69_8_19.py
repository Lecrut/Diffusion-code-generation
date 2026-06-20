import time

class FastAccessList:
    def __init__(self, data):
        self.data = {i: value for i, value in enumerate(data)}

    def __getitem__(self, index):
        return self.data[index]

def benchmark_access():
    sample_data = list(range(1000000))
    fast_list = FastAccessList(sample_data)
    
    start_time = time.time()
    for _ in range(100000):
        _ = sample_data[50000]
    list_time = time.time() - start_time
    
    start_time = time.time()
    for _ in range(100000):
        _ = fast_list[50000]
    fast_access_time = time.time() - start_time
    
    print(f"Standard Python List Access Time: {list_time:.6f} seconds")
    print(f"Custom FastAccessList Access Time: {fast_access_time:.6f} seconds")

if __name__ == '__main__':
    benchmark_access()