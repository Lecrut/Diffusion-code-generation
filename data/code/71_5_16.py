def middle_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
        second = next(iterator)
        while True:
            yield second
            first, second = (second, next(iterator))
    except StopIteration:
        if first == second:
            yield first
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = middle_element_generator(data1)
    print(next(gen1))
    data2 = [10, 20, 30, 40]
    gen2 = middle_element_generator(data2)
    print(next(gen2))
    data3 = [100]
    gen3 = middle_element_generator(data3)
    try:
        print(next(gen3))
    except StopIteration:
        print('No element')