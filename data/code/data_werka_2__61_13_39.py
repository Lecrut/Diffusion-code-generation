class SafeListAccess:

    def __init__(self, elements):
        self.elements = elements

    def get_element_at_index(self, index):
        if 0 <= index < len(self.elements):
            return self.elements[index]
        else:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    safe_access = SafeListAccess(sample_list)
    index_to_access = 3
    result = safe_access.get_element_at_index(index_to_access)
    print(result)
    out_of_bounds_index = 10
    result_out_of_bounds = safe_access.get_element_at_index(out_of_bounds_index)
    print(result_out_of_bounds)
    negative_index = -1
    negative_result = safe_access.get_element_at_index(negative_index)
    print(negative_result)
    zero_index = 0
    zero_result = safe_access.get_element_at_index(zero_index)
    print(zero_result)