def get_first_and_last(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return
    
    last = None
    for item in iterator:
        last = item
    
    yield first
    if last is not None:
        yield last

if __name__ == '__main__':
    sample_values1 = [1, 2, 3, 4, 5]
    print(list(get_first_and_last(sample_values1)))
    
    sample_values2 = [10]
    print(list(get_first_and_last(sample_values2)))
    
    sample_values3 = [100]
    print(list(get_first_and_last(sample_values3)))