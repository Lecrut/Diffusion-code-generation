def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list
    
    def access(self, index):
        return get_element_at_index(self.data_list, index)

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_list)
    
    indices_to_test = [2, 5, -1, 0]
    for idx in indices_to_test:
        print(accessor.access(idx))