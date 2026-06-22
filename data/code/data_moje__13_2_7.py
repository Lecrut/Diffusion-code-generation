class InvalidIndexError(Exception):
    def __init__(self, message):
        super().__init__(message)

def extract_item_by_index(t, index):
    if not isinstance(index, int):
        raise InvalidIndexError("Index must be an integer")
    if index < 0 or index >= len(t):
        raise InvalidIndexError(f"Index {index} is out of range for tuple of length {len(t)}")
    return t[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = extract_item_by_index(sample_tuple, 2)
    print(result)
    try:
        extract_item_by_index(sample_tuple, 5)
    except InvalidIndexError as e:
        print(e)