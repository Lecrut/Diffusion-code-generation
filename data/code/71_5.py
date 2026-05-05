def middle_element_generator(iterable):
    n = len(iterable)
    if n == 0:
        return
    start = n // 2
    if n % 2 == 1:
        yield iterable[start]
    else:
        yield iterable[start - 1]
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = middle_element_generator(data1)
    print(list(gen1))
    data2 = [10, 20, 30, 40]
    gen2 = middle_element_generator(data2)
    print(list(gen2))
    data3 = [100]
    gen3 = middle_element_generator(data3)
    print(list(gen3))
    data4 = []
    gen4 = middle_element_generator(data4)
    print(list(gen4))