class SafeListAccess:

    def __init__(self, data):
        self.data = data

    def get_element_at_index(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    safe_access = SafeListAccess(sample_list)
    index_to_access = 2
    result = safe_access.get_element_at_index(index_to_access)
    print(result)
    out_of_bounds_index = 10
    result_out_of_bounds = safe_access.get_element_at_index(out_of_bounds_index)
    print(result_out_of_bounds)
    negative_index = -1
    result_negative_index = safe_access.get_element_at_index(negative_index)
    print(result_negative_index)
    zero_index = 0
    result_zero_index = safe_access.get_element_at_index(zero_index)
    print(result_zero_index)