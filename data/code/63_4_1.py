def first_element_generator(iterable):
    try:
        yield next(iter(iterable))
    except StopIteration:
        pass
if __name__ == '__main__':
    data1 = [1, 2, 3, 4]
    gen1 = first_element_generator(data1)
    result1 = list(gen1)
    print(result1)
    data2 = "hello"
    gen2 = first_element_generator(data2)
    result2 = list(gen2)
    print(result2)
    data3 = []
    gen3 = first_element_generator(data3)
    result3 = list(gen3)
    print(result3)