def get_middle_index(iterator):
    length = sum(1 for _ in iterator)
    return (length - 1) // 2 if length > 0 else None
if __name__ == '__main__':
    data_gen = iter([1, 2, 3, 4, 5])
    index = get_middle_index(data_gen)
    print(index)