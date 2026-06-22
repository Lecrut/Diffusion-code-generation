class TupleAccessError(Exception):
    def __init__(self, idx, size):
        self.idx = idx
        self.size = size
        message = f"Cannot access index {idx} in tuple of size {size}"
        super().__init__(message)

def retrieve_element(data_tuple, target_idx):
    total_len = len(data_tuple)
    if total_len == 0:
        raise TupleAccessError(target_idx, 0)
    lower = -total_len
    upper = total_len - 1
    if target_idx < lower or target_idx > upper:
        raise TupleAccessError(target_idx, total_len)
    return data_tuple[target_idx]

def main_runner():
    test_values = ("red", "green", "blue", "yellow", "orange")
    idx_to_fetch = 3
    retrieved = retrieve_element(test_values, idx_to_fetch)
    print(retrieved)
    try:
        retrieve_element(test_values, 10)
    except TupleAccessError as err:
        print(f"Error caught: {err}")

if __name__ == '__main__':
    main_runner()