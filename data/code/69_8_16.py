import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def main():
    sample_size = 1000000
    standard_list = list(range(sample_size))
    fast_list = FastList(list(range(sample_size)))
    start_time = time.time()
    for i in range(sample_size):
        _ = standard_list[i]
    standard_list_access_time = time.time() - start_time
    start_time = time.time()
    for i in range(sample_size):
        _ = fast_list.get(i)
    fast_list_access_time = time.time() - start_time
    print(f'Standard list access time: {standard_list_access_time:.6f} seconds')
    print(f'FastList access time: {fast_list_access_time:.6f} seconds')
if __name__ == '__main__':
    main()