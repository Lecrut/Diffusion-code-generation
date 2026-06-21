class InvalidIndexError(Exception):
    def __init__(self, index, length):
        self.index = index
        self.length = length
        super().__init__(f"Index {index} is out of range for tuple of length {length}")

def extract_item_by_index(tup, index):
    length = len(tup)
    if index < 0 or index >= length:
        raise InvalidIndexError(index, length)
    return tup[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = extract_item_by_index(sample_tuple, 2)
    print(result)