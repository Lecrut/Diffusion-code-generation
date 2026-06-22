def get_middle(iterable):
    if hasattr(iterable, '__len__'):
        length = len(iterable)
        if length == 0:
            return None
        indices = {
            'odd': lambda n: n // 2,
            'even': lambda n: n // 2 - 1
        }
        target_index = indices['odd'](length) if length % 2 else indices['even'](length)
        for i, item in enumerate(iterable):
            if i == target_index:
                return item
        return None
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return None
    second = first
    for item in iterator:
        second = item
    return second

if __name__ == '__main__':
    list_data = [10, 20, 30, 40, 50]
    result1 = get_middle(list_data)
    print(result1)
    tuple_data = (100, 200, 300, 400)
    result2 = get_middle(tuple_data)
    print(result2)
    empty_list = []
    result3 = get_middle(empty_list)
    print(result3)