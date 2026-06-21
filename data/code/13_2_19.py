class OutOfBoundsIndexError(Exception):
    def __init__(self, requested_index, available_length):
        self.requested_index = requested_index
        self.available_length = available_length
        super().__init__(f"Index {requested_index} exceeds bounds of tuple with length {available_length}.")

def validate_tuple_index(tup, index):
    if not isinstance(index, int) or isinstance(index, bool):
        raise OutOfBoundsIndexError(index, len(tup))
    total_len = len(tup)
    if index < -total_len or index >= total_len:
        raise OutOfBoundsIndexError(index, total_len)

def get_element_at_index(tup, index):
    validate_tuple_index(tup, index)
    return tup[index]

if __name__ == '__main__':
    data_source = (5, 15, 25, 35, 45)
    target_pos = 3
    extracted_value = get_element_at_index(data_source, target_pos)
    print(extracted_value)
    try:
        bad_pos = 100
        get_element_at_index(data_source, bad_pos)
    except OutOfBoundsIndexError as error_instance:
        print(error_instance.args[0])