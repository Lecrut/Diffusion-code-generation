def find_middle_index(iterable):
    length = sum(1 for _ in iterable)
    return (length - 1) // 2 if length > 0 else None
if __name__ == '__main__':
    data_gen = range(9)
    middle_idx = find_middle_index(data_gen)
    print(middle_idx)