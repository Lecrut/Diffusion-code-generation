import time

class FastList:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def main():
    sample_data = list(range(1000000))
    start_time = time.time()
    for i in range(len(sample_data)):
        _ = sample_data[i]
    end_time = time.time()
    print(f'Time taken to access elements in a standard Python list: {end_time - start_time:.6f} seconds')
    fast_list = FastList(sample_data)
    start_time = time.time()
    for i in range(len(sample_data)):
        _ = fast_list.get(i)
    end_time = time.time()
    print(f'Time taken to access elements in a FastList: {end_time - start_time:.6f} seconds')
if __name__ == '__main__':
    main()