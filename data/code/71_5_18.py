def _validate_iterable(obj):
    if obj is None:
        raise ValueError("Input cannot be None")
    if not hasattr(obj, '__iter__'):
        raise ValueError("Input must be an iterable")
    return obj

def middle_element_generator(iterable):
    _validate_iterable(iterable)
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return
    try:
        second = next(iterator)
    except StopIteration:
        yield first
        return
    left = first
    right = second
    while True:
        try:
            current = next(iterator)
            left = right
            right = current
        except StopIteration:
            if right is not left:
                yield left
            return

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [100, 200, 300, 400]
    single_list = [42]
    empty_list = []

    result_odd = list(middle_element_generator(odd_list))
    result_even = list(middle_element_generator(even_list))
    result_single = list(middle_element_generator(single_list))
    result_empty = list(middle_element_generator(empty_list))

    print(result_odd)
    print(result_even)
    print(result_single)
    print(result_empty)