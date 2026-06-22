class InvalidTupleIndexError(Exception):
    def __init__(self, index, length):
        self.index = index
        self.length = length
        super().__init__(f"Index {index} is out of bounds for tuple of length {length}")

def extract_item_by_index(tup, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(tup):
        raise InvalidTupleIndexError(index, len(tup))
    return tup[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_item_by_index(sample_tuple, 2))
    print(extract_item_by_index(sample_tuple, 0))
    print(extract_item_by_index(sample_tuple, 4))