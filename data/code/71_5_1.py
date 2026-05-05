def middle_element_generator(iterable):
    n = len(iterable)
    if n == 0:
        return
    start = n // 2
    for i in range(n):
        if i == start:
            yield iterable[i]
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = middle_element_generator(data1)
    print(list(gen1))
    data2 = [10, 20, 30, 40, 50, 60]
    gen2 = middle_element_generator(data2)
    print(list(gen2))
    data3 = [1, 2, 3, 4]
    gen3 = middle_element_generator(data3)
    print(list(gen3))
    data4 = [100]
    gen4 = middle_element_generator(data4)
    print(list(gen4))
    data5 = []
    gen5 = middle_element_generator(data5)
    print(list(gen5))