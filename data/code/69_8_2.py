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
    standard_list_time = time.time() - start_time
    fast_list = FastList(sample_data)
    start_time = time.time()
    for i in range(len(sample_data)):
        _ = fast_list.get(i)
    fast_list_time = time.time() - start_time
    print(f'Standard Python list access time: {standard_list_time:.6f} seconds')
    print(f'Custom FastList access time: {fast_list_time:.6f} seconds')
if __name__ == '__main__':
    main()