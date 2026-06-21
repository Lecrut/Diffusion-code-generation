class TupleAccessError(Exception):
    def __init__(self, idx, total):
        self.idx = idx
        self.total = total
        super().__init__(f"Access failed: index {idx} invalid for sequence of size {total}")

def validate_bounds(seq, idx):
    size = len(seq)
    if not isinstance(idx, int) or isinstance(idx, bool):
        raise TupleAccessError(idx, size)
    if idx < -size or idx >= size:
        raise TupleAccessError(idx, size)

def retrieve_element(container, position):
    validate_bounds(container, position)
    return container[position]

def run_demo():
    data_set = ("red", "green", "blue", "yellow", "orange")
    try:
        val = retrieve_element(data_set, 2)
        print(val)
    except TupleAccessError:
        print("Error retrieving element")

    try:
        retrieve_element(data_set, 10)
    except TupleAccessError as err:
        print(f"Caught expected error: {err}")

if __name__ == '__main__':
    run_demo()