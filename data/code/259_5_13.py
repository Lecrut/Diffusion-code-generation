def find_min_max(iterable):
    if not iterable:
        return None, None
    current_min = current_max = next(iter(iterable))
    for item in iterable:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    return current_min, current_max

if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    print("Data 1:", find_min_max(data1))