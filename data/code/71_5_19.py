def middle_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
        second = next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")
    
    for item in iterator:
        yield first
        first, second = second, item
    
    yield second

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(next(middle_element_generator(sample_values)))