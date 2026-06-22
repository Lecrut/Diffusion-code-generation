class TupleIndexOutOfRangeError(Exception):
    def __init__(self, index, length):
        self.index = index
        self.length = length
        message = f"Index {index} exceeds tuple length {length}"
        super().__init__(message)

def validate_index(index, length):
    if not isinstance(index, int) or isinstance(index, bool):
        raise TypeError("Index must be an integer")
    if index < -length or index >= length:
        raise TupleIndexOutOfRangeError(index, length)

def retrieve_tuple_item(tup, index):
    validate_index(index, len(tup))
    return tup[index]

if __name__ == '__main__':
    dataset = ("apple", "banana", "cherry", "date", "elderberry")
    target_index = 3
    retrieved_value = retrieve_tuple_item(dataset, target_index)
    print(retrieved_value)
    try:
        retrieve_tuple_item(dataset, 7)
    except TupleIndexOutOfRangeError as error:
        print(error)