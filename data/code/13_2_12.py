class OutOfBoundsError(Exception):
    def __init__(self, provided_index, tuple_length):
        self.provided_index = provided_index
        self.tuple_length = tuple_length
        message = f"Index {provided_index} is invalid for tuple of length {tuple_length}"
        super().__init__(message)

def validate_integer_index(value):
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return False

def check_bounds(index, length):
    lower_limit = -length
    upper_limit = length - 1
    if index < lower_limit:
        return False
    if index > upper_limit:
        return False
    return True

def get_item_at_index(source_tuple, target_index):
    if not validate_integer_index(target_index):
        raise OutOfBoundsError(target_index, len(source_tuple))
    total_items = len(source_tuple)
    if not check_bounds(target_index, total_items):
        raise OutOfBoundsError(target_index, total_items)
    return source_tuple[target_index]

if __name__ == '__main__':
    data_tuple = ('apple', 'banana', 'cherry', 'date')
    index_to_fetch = 1
    retrieved_value = get_item_at_index(data_tuple, index_to_fetch)
    print(retrieved_value)
    try:
        get_item_at_index(data_tuple, 5)
    except OutOfBoundsError as error:
        print(error)