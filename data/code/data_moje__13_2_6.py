class OutOfBoundsError(Exception):
    def __init__(self, idx, size):
        self.idx = idx
        self.size = size
        super().__init__(f"Index {idx} is out of bounds for size {size}")

def _is_valid_index(index, length):
    return isinstance(index, int) and not isinstance(index, bool) and -length <= index < length

def pick_element(tup, index):
    length = len(tup)
    if not _is_valid_index(index, length):
        raise OutOfBoundsError(index, length)
    return tup[index]

if __name__ == '__main__':
    data = (1, 2, 3, 4, 5)
    print(pick_element(data, 0))
    print(pick_element(data, -1))
    try:
        pick_element(data, 10)
    except OutOfBoundsError as ex:
        print(ex.idx, ex.size)