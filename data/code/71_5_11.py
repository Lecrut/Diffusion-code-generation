def middle_element_generator(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return None
    second = None
    for item in it:
        if second is not None:
            yield second
        second = first
        first = item
    yield first

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(next(middle_element_generator(sample_values)))