def first_element_generator(iterable):
    def validate_iterable(it):
        if not hasattr(it, '__iter__'):
            raise ValueError("The provided object is not iterable")
    
    validate_iterable(iterable)
    iterator = iter(iterable)
    try:
        yield next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    sample_iterable = [42, 84, 126, 168, 210]
    generator = first_element_generator(sample_iterable)
    print(next(generator))