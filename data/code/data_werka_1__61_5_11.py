def element_at_position(iterable, position):
    try:
        if position < 0:
            raise ValueError("Position must be a non-negative integer.")
        for index, item in enumerate(iterable):
            if index == position:
                yield item
    except TypeError:
        raise TypeError("The iterable must be an iterable list or tuple.")

if __name__ == '__main__':
    LARGE_LIST_SIZE = 1000000
    TARGET_INDEX = 500000
    large_list = list(range(LARGE_LIST_SIZE))
    generator = element_at_position(large_list, TARGET_INDEX)
    result = next(generator, None)
    print(result)