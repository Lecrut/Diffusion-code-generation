def first_last_elements(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return None, None
    last = first
    for element in iterator:
        last = element
    return first, last

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(first_last_elements(sample_values))