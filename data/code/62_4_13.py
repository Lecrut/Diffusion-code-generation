def second_element_generator(iterable):
    iterator = iter(iterable)
    next(iterator, None)
    for item in iterator:
        yield item
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    generator = second_element_generator(sample_data)
    for value in generator:
        print(value)