def calculate_center(iterable):
    if not iterable:
        return None
    total = sum(1 for _ in iterable)
    mid = total // 2
    return mid
if __name__ == '__main__':
    sample_iterable = (1, 2, 3, 4)
    center_index = calculate_center(sample_iterable)
    print(center_index)