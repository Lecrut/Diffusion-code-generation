def position_generator(data, index):
    if not isinstance(data, (list, tuple)):
        raise TypeError("The data must be an iterable list or tuple.")
    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer.")
    
    for i, item in enumerate(data):
        if i == index:
            yield item

if __name__ == '__main__':
    large_list = list(range(1000000))
    target_index = 500000
    try:
        generator = position_generator(large_list, target_index)
        result = next(generator, None)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)