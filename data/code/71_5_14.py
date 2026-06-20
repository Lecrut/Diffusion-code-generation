def middle_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return None
    try:
        second = next(iterator)
    except StopIteration:
        return first
    prev, current = first, second
    for _ in iterator:
        prev, current = current, next(iterator)
    if len(iterable) % 2 == 0:
        yield (prev + current) / 2
    else:
        yield current

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(next(middle_element_generator(sample_values)))