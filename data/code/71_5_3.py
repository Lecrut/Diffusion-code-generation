def middle_element_generator(iterable):
    n = len(iterable)
    if n == 0:
        return
    middle_index = n // 2
    for item in iterable:
        if middle_index == 0:
            yield item
        elif middle_index == n - 1:
            yield item
        else:
            if middle_index == n // 2:
                yield item
            else:
                yield None
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = middle_element_generator(data1)
    print("Data 1:", list(gen1))
    data2 = [10, 20, 30, 40, 50, 60]
    gen2 = middle_element_generator(data2)
    print("Data 2:", list(gen2))
    data3 = [100]
    gen3 = middle_element_generator(data3)
    print("Data 3:", list(gen3))
    data4 = [1, 2, 3, 4]
    gen4 = middle_element_generator(data4)
    print("Data 4:", list(gen4))
    data5 = []
    gen5 = middle_element_generator(data5)
    print("Data 5:", list(gen5))