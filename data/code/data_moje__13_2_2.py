class TupleIndexError(Exception):
    def __init__(self, index, data_len):
        self.index = index
        self.data_len = data_len
        super().__init__(f"Index {index} is invalid for tuple of length {data_len}")

def get_tuple_element(source_tuple, target_index):
    element_count = len(source_tuple)
    min_idx = -element_count
    max_idx = element_count - 1
    if not isinstance(target_index, int) or isinstance(target_index, bool):
        raise TupleIndexError(target_index, element_count)
    if target_index < min_idx or target_index > max_idx:
        raise TupleIndexError(target_index, element_count)
    return source_tuple[target_index]

if __name__ == '__main__':
    test_data = ('alpha', 'beta', 'gamma', 'delta')
    selected_item = get_tuple_element(test_data, 2)
    print(selected_item)
    try:
        get_tuple_element(test_data, 5)
    except TupleIndexError as e:
        print(f"Error: {e.message if hasattr(e, 'message') else str(e)}")