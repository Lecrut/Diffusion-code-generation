import time

class FastList:
    def __init__(self, elements):
        self.elements = list(elements)

    def get(self, index):
        return self.elements[index]

def access_list_elements(data_structure, indices):
    start_time = time.time()
    for index in indices:
        data_structure.get(index)
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    sample_data = list(range(10000))
    fast_list_instance = FastList(sample_data)
    standard_list = sample_data
    indices_to_access = [i for i in range(0, 10000, 10)]

    time_fast_list = access_list_elements(fast_list_instance, indices_to_access)
    time_standard_list = access_list_elements(standard_list, indices_to_access)

    print("Time taken by FastList:", time_fast_list)
    print("Time taken by standard list:", time_standard_list)