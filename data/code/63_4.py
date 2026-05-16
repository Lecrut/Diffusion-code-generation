def first_element_generator(iterable):
    try:
        yield next(iter(iterable))
    except StopIteration:
        pass
if __name__ == '__main__':
    sample1 = [1, 2, 3, 4]
    gen1 = first_element_generator(sample1)
    print(list(gen1))
    sample2 = "hello"
    gen2 = first_element_generator(sample2)
    print(list(gen2))
    sample3 = []
    gen3 = first_element_generator(sample3)
    print(list(gen3))