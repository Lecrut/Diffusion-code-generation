class CustomTupleIndexError(Exception):
    def __init__(self, index, tuple_length):
        self.index = index
        self.length = tuple_length
        super().__init__(f"Index {index} is invalid for tuple of length {tuple_length}.")

def fetch_tuple_element(source_tuple, target_index):
    tuple_length = len(source_tuple)
    min_index = -tuple_length
    max_index = tuple_length - 1
    
    if not isinstance(target_index, int) or isinstance(target_index, bool):
        raise CustomTupleIndexError(target_index, tuple_length)
    
    if target_index < min_index or target_index > max_index:
        raise CustomTupleIndexError(target_index, tuple_length)
    
    return source_tuple[target_index]

if __name__ == '__main__':
    test_data = (1, 2, 3, 4, 5)
    index_to_use = 3
    result = fetch_tuple_element(test_data, index_to_use)
    print(result)
    try:
        fetch_tuple_element(test_data, 100)
    except CustomTupleIndexError as e:
        print(f"Caught expected error: {e}")
        print(f"Index was: {e.index}, Length was: {e.length}")