def element_at_position(iterable, position):
    if not isinstance(position, int) or position < 0:
        raise ValueError("Position must be a non-negative integer.")
    
    for index, item in enumerate(iterable):
        if index == position:
            yield item

if __name__ == '__main__':
    SAMPLE_LIST = list(range(1000000))
    TARGET_INDEX = 500000
    
    try:
        generator = element_at_position(SAMPLE_LIST, TARGET_INDEX)
        result = next(generator, None)
        print(result)
    except ValueError as e:
        print(e)