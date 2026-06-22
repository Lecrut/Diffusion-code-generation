class OutOfBoundsError(Exception):
    def __init__(self, idx, size):
        self.idx = idx
        self.size = size
        super().__init__(f"Index {idx} is invalid for tuple of size {size}")

def _is_valid_index(idx, size):
    if not isinstance(idx, int) or isinstance(idx, bool):
        return False
    if idx < -size or idx >= size:
        return False
    return True

def pick_element(source, position):
    count = len(source)
    if not _is_valid_index(position, count):
        raise OutOfBoundsError(position, count)
    return source[position]

if __name__ == '__main__':
    sample_data = (5, 15, 25, 35, 45)
    target_idx = 3
    value = pick_element(sample_data, target_idx)
    print(value)
    error_idx = -10
    try:
        pick_element(sample_data, error_idx)
    except OutOfBoundsError as exc:
        print(exc)