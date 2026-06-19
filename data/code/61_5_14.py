def fetch_at_position(iterable, position):
    if not isinstance(position, int) or position < 0:
        raise ValueError("Position must be a non-negative integer.")
    for index, item in enumerate(iterable):
        if index == position:
            yield item

if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    try:
        generator = fetch_at_position(large_list, target_index)
        result = next(generator, None)
        print(result)
    except ValueError as e:
        print(e)