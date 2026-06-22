class InvalidTupleIndexError(Exception):
    def __init__(self, index, length):
        super().__init__(f"Index {index} is out of bounds for tuple of length {length}.")
        self.index = index
        self.length = length

def extract_by_index(tup, index):
    if not isinstance(index, int):
        raise InvalidTupleIndexError(index, len(tup))
    if index < -len(tup) or index >= len(tup):
        raise InvalidTupleIndexError(index, len(tup))
    return tup[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    valid_index = 2
    result = extract_by_index(sample_tuple, valid_index)
    print(result)
    try:
        extract_by_index(sample_tuple, 10)
    except InvalidTupleIndexError as e:
        print(e)