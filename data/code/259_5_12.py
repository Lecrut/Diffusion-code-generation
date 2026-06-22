def find_min_max(iterable):
    try:
        first_item = next(iter(iterable))
    except StopIteration:
        return None, None
    current_min = current_max = first_item
    for item in iterable:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    return current_min, current_max

if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    min_val, max_val = find_min_max(data1)
    print(f"Min: {min_val}, Max: {max_val}")