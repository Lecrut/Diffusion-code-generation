class OutOfRangeError(Exception):
    def __init__(self, idx, size):
        self.idx = idx
        self.size = size
        super().__init__(f"Index {idx} exceeds the bounds of a tuple with length {size}")

def validate_bounds(current_tuple, target_idx):
    bound_min = -len(current_tuple)
    bound_max = len(current_tuple) - 1
    if not isinstance(target_idx, int) or isinstance(target_idx, bool):
        raise TypeError("Index must be an integer")
    if target_idx < bound_min or target_idx > bound_max:
        raise OutOfRangeError(target_idx, len(current_tuple))
    return True

def retrieve_item(data_tuple, position):
    validate_bounds(data_tuple, position)
    return data_tuple[position]

if __name__ == '__main__':
    inventory = ('hammer', 'wrench', 'screwdriver', 'pliers', 'tape')
    try:
        item = retrieve_item(inventory, 2)
        print(item)
    except OutOfRangeError as e:
        print(f"Error: {e}")

    try:
        bad_item = retrieve_item(inventory, 15)
        print(bad_item)
    except OutOfRangeError as e:
        print(f"Error: {e}")