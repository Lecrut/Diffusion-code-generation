class BadTupleIndexException(Exception):
    def __init__(self, requested_index, tuple_length):
        self.requested_index = requested_index
        self.tuple_length = tuple_length
        message = f"Invalid index {requested_index} for tuple of length {tuple_length}"
        super().__init__(message)

def _is_valid_index(index, length):
    if not isinstance(index, int) or isinstance(index, bool):
        return False
    if index < -length or index >= length:
        return False
    return True

def pick_element(t, i):
    length = len(t)
    if not _is_valid_index(i, length):
        raise BadTupleIndexException(i, length)
    return t[i]

if __name__ == '__main__':
    data = (5, 15, 25, 35, 45)
    target = 1
    value = pick_element(data, target)
    print(value)
    try:
        pick_element(data, 100)
    except BadTupleIndexException as err:
        print(err)