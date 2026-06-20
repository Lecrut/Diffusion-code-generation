def middle_element_generator(iterable):
    it = iter(iterable)
    try:
        first = next(it)
        second = next(it)
    except StopIteration:
        raise ValueError("Iterable is empty")
    
    for item in it:
        yield second
        first, second = second, item
    
    yield second

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(next(middle_element_generator(sample_values)))