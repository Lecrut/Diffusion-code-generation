class BoundsError(Exception):
    def __init__(self, requested_index, container_size):
        self.requested = requested_index
        self.size = container_size
        message = f"Requested index {requested_index} exceeds container size {container_size}"
        super().__init__(message)

def validate_index(index, length):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if length == 0:
        return False
    if index < 0:
        return -index <= length
    return index < length

def safe_extract(data_tuple, target_index):
    container_length = len(data_tuple)
    is_valid = validate_index(target_index, container_length)
    if not is_valid:
        raise BoundsError(target_index, container_length)
    return data_tuple[target_index]

def main_runner():
    items = ("apple", "banana", "cherry", "date", "elderberry")
    index_ok = 1
    index_fail = -6
    print(safe_extract(items, index_ok))
    try:
        safe_extract(items, index_fail)
    except BoundsError as err:
        print(err)

if __name__ == '__main__':
    main_runner()