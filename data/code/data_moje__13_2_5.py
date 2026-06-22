class BadTupleAccessError(Exception):
    def __init__(self, idx, bound):
        self.idx_val = idx
        self.bound_val = bound
        super().__init__(f"Index {idx} invalid for size {bound}")

def safe_fetch(item_container, position):
    total_items = len(item_container)
    if not isinstance(position, int) or isinstance(position, bool):
        raise BadTupleAccessError(position, total_items)
    if position < -total_items or position >= total_items:
        raise BadTupleAccessError(position, total_items)
    return item_container[position]

if __name__ == '__main__':
    data_set = (10, 20, 30, 40, 50)
    print(safe_fetch(data_set, 1))
    print(safe_fetch(data_set, -1))
    try:
        safe_fetch(data_set, 99)
    except BadTupleAccessError:
        print("Caught bad index error")