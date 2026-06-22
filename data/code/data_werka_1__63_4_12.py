def first_element_generator(iterable):
    for item in iterable:
        yield item
        break

if __name__ == '__main__':
    sample_iterable = [42, 84, 168]
    generator = first_element_generator(sample_iterable)
    print(next(generator))