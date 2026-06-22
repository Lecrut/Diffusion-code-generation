class ListAccessor:
    DEFAULT_LIST = ["apple", "banana", "cherry", "date"]
    
    @staticmethod
    def get_element_by_position(lst, index):
        try:
            return lst[index]
        except IndexError:
            return None

if __name__ == '__main__':
    accessor = ListAccessor()
    sample_list = [10, 20, 30, 40, 50]
    index_to_fetch = 3
    element = accessor.get_element_by_position(sample_list, index_to_fetch)
    print(element)
    out_of_bounds_index = 10
    element_out_of_bounds = accessor.get_element_by_position(sample_list, out_of_bounds_index)
    print(element_out_of_bounds)