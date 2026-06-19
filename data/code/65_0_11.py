class ListAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get_element_by_position(self, index):
        try:
            return self.elements[index]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    accessor = ListAccessor(sample_list)
    index_to_fetch = 2
    element = accessor.get_element_by_position(index_to_fetch)
    print(element)
    out_of_bounds_index = 10
    element_out_of_bounds = accessor.get_element_by_position(out_of_bounds_index)
    print(element_out_of_bounds)