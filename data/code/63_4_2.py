def first_element_generator(iterable):
    try:
        yield next(iter(iterable))
    except StopIteration:
        pass
if __name__ == '__main__':
    my_list = [10, 20, 30]
    gen1 = first_element_generator(my_list)
    print(list(gen1))
    my_tuple = (5, 15, 25)
    gen2 = first_element_generator(my_tuple)
    print(list(gen2))
    empty_list = []
    gen3 = first_element_generator(empty_list)
    print(list(gen3))