class TupleIndexError(Exception):
    def __init__(self, index, length):
        self.index = index
        self.length = length
        super().__init__(f"Invalid index {index} for tuple of length {length}")

def get_element(source_tuple, target_index):
    length = len(source_tuple)
    if not isinstance(target_index, int) or isinstance(target_index, bool):
        raise TupleIndexError(target_index, length)
    if target_index < -length or target_index >= length:
        raise TupleIndexError(target_index, length)
    return source_tuple[target_index]

if __name__ == '__main__':
    test_data = ('alpha', 'beta', 'gamma', 'delta')
    selected_item = get_element(test_data, 1)
    print(selected_item)
    try:
        get_element(test_data, 4)
    except TupleIndexError as e:
        print(f"Caught error: {e}")