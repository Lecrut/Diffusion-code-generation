class IndexOutOfBoundsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def extract_item(tup, idx):
    lower_bound = -len(tup)
    upper_bound = len(tup) - 1
    if not isinstance(idx, int) or isinstance(idx, bool):
        raise IndexOutOfBoundsError("Index must be an integer.")
    if idx < lower_bound or idx > upper_bound:
        raise IndexOutOfBoundsError(f"Index {idx} out of bounds for length {len(tup)}.")
    return tup[idx]

if __name__ == '__main__':
    data = (100, 200, 300, 400, 500)
    valid_result = extract_item(data, 1)
    print(valid_result)
    try:
        extract_item(data, 10)
    except IndexOutOfBoundsError as e:
        print(e.message)