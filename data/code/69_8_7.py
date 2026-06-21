import time

class FastList:
    def __init__(self, elements):
        self.elements = elements
    
    @staticmethod
    def access_time(elements, access_method):
        start_time = time.time()
        for i in range(len(elements)):
            _ = access_method(i)
        return time.time() - start_time
    
    def get(self, index):
        return self.elements[index]

def standard_list_access(elements, index):
    return elements[index]

if __name__ == '__main__':
    sample_size = 1000000
    sample_data = list(range(sample_size))
    
    standard_list_time = FastList.access_time(
        sample_data,
        lambda index: standard_list_access(sample_data, index)
    )
    
    fast_list = FastList(sample_data)
    fast_list_time = FastList.access_time(
        sample_data,
        lambda index: fast_list.get(index)
    )
    
    print(f'Standard Python list access time: {standard_list_time:.6f} seconds')
    print(f'Custom FastList access time: {fast_list_time:.6f} seconds')