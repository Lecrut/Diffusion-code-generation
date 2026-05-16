def second_element_generator(iterable):
    it = iter(iterable)
    try:
        first = next(it)
        yield next(it)
    except StopIteration:
        return
if __name__ == '__main__':
    data1 = [10, 20, 30, 40]
    gen1 = second_element_generator(data1)
    print(list(gen1))
    data2 = [5, 15]
    gen2 = second_element_generator(data2)
    print(list(gen2))
    data3 = [1]
    gen3 = second_element_generator(data3)
    print(list(gen3))
    data4 = []
    gen4 = second_element_generator(data4)
    print(list(gen4))