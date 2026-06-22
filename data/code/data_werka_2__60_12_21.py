def last_element_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            last = next(iterator)
    except StopIteration:
        yield last
if __name__ == '__main__':
    sample_sequence = range(1000000)
    for element in last_element_generator(sample_sequence):
        print(element)