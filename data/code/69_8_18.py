import time

class FastList:
    def __init__(self, elements):
        self.elements = elements

    @staticmethod
    def access_time(elements, method):
        start_time = time.time()
        for i in range(len(elements)):
            if method == 'standard':
                _ = elements[i]
            elif method == 'fast':
                _ = FastList(elements).get(i)
        return time.time() - start_time

    def get(self, index):
        return self.elements[index]

def main():
    sample_size = 1000000
    sample_data = list(range(sample_size))
    
    standard_list_time = FastList.access_time(sample_data, 'standard')
    fast_list_time = FastList.access_time(sample_data, 'fast')
    
    print(f'Standard Python list access time: {standard_list_time:.6f} seconds')
    print(f'FastList access time: {fast_list_time:.6f} seconds')

if __name__ == '__main__':
    main()