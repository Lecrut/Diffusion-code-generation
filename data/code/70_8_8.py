def check_endpoints(iterable):
    items = tuple(iterable)
    if not items:
        return None, None
    start_item = items[0]
    end_item = items[-1]
    return start_item, end_item

if __name__ == '__main__':
    data_sequence = "algorithm"
    head, tail = check_endpoints(data_sequence)
    print(head, tail)
    data_tuple = (100, 200, 300)
    first, last = check_endpoints(data_tuple)
    print(first, last)
    empty_data = set()
    x, y = check_endpoints(empty_data)
    print(x, y)