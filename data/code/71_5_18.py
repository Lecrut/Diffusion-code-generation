def middle_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return None

    second = None
    for element in iterator:
        if second is not None:
            yield second
            second = None
        else:
            second = first
        first = element

    if second is not None:
        yield second

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(next(middle_element_generator(sample_values)))