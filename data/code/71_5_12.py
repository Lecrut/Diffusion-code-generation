def middle_element_generator(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return None
    try:
        second = next(it)
    except StopIteration:
        return first
    prev, current = first, second
    for item in it:
        prev, current = current, item
    if len(iterable) % 2 == 0:
        yield (prev + current) / 2
    else:
        yield current

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(next(middle_element_generator(sample_values)))