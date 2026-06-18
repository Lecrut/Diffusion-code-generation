def middle_index_generator(iterable):
    iterator = iter(iterable)
    total_count = 0
    try:
        while True:
            item = next(iterator)
            _ = item                                                                     
            total_count += 1
    except StopIteration:
        pass
    middle_index = (total_count - 1) // 2
def get_middle_position(iterable):
    if not iterable:
        return None
    iterator = iter(iterable)
    count = sum(1 for _ in iterator)
    middle_index = (count - 1) // 2
    return middle_index
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_position(sample_list)
    print(result)