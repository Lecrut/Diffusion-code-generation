import time

class FastIndexList:
    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        return self.elements[index]

def access_list_elements(lst, indices):
    start_time = time.time()
    for index in indices:
        lst[index]
    end_time = time.time()
    return end_time - start_time

def access_fast_index_list(fast_lst, indices):
    start_time = time.time()
    for index in indices:
        fast_lst.get(index)
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    sample_size = 10000
    indices_to_access = [i % sample_size for i in range(1000)]
    
    standard_list = list(range(sample_size))
    fast_index_list = FastIndexList(list(range(sample_size)))
    
    time_standard_list = access_list_elements(standard_list, indices_to_access)
    time_fast_index_list = access_fast_index_list(fast_index_list, indices_to_access)
    
    print("Time taken to access elements in standard list:", time_standard_list)
    print("Time taken to access elements in fast index list:", time_fast_index_list)