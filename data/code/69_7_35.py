import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def main():
    sample_size = 1000000
    sample_list = list(range(sample_size))
    fast_list = FastList(sample_list)
    start_time = time.time()
    for i in range(sample_size):
        _ = sample_list[i]
    end_time = time.time()
    std_list_time = end_time - start_time
    start_time = time.time()
    for i in range(sample_size):
        _ = fast_list.get(i)
    end_time = time.time()
    fast_list_time = end_time - start_time
    print(f'Standard List Access Time: {std_list_time} seconds')
    print(f'FastList Access Time: {fast_list_time} seconds')
if __name__ == '__main__':
    main()