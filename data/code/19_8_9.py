import random

def get_random_value(index_range, values):
    if not index_range or not values:
        return None
    if not values:
        return None
    if index_range.start is not None and index_range.stop is not None and index_range.step is not None:
        step = index_range.step
        if step <= 0:
            raise ValueError("Step must be positive")
    if not isinstance(index_range, range):
        raise TypeError("First argument must be a range object")
    if not isinstance(values, list):
        raise TypeError("Second argument must be a list")
    if len(values) == 0:
        return None
    start = index_range.start if index_range.start is not None else 0
    stop = index_range.stop
    step = index_range.step if index_range.step is not None else 1
    if start >= stop:
        raise ValueError("Range must have valid length")
    length = len(range(start, stop, step))
    if length == 0:
        raise ValueError("Range is empty")
    random_index = random.randrange(length)
    actual_index = start + random_index * step
    if actual_index >= len(values):
        raise IndexError("Index out of bounds for values list")
    return values[actual_index]

if __name__ == '__main__':
    values_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    index_range = range(0, 5, 1)
    result = get_random_value(index_range, values_list)
    print(result)