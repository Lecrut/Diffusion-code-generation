def first_element_generator(iterable):
    try:
        yield next(iter(iterable))
    except StopIteration:
        pass
if __name__ == '__main__':
    data1 = [1, 2, 3, 4]
    gen1 = first_element_generator(data1)
    print(list(gen1))
    data2 = "hello"
    gen2 = first_element_generator(data2)
    print(list(gen2))
    data3 = []
    gen3 = first_element_generator(data3)
    print(list(gen3))