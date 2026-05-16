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
            if middle_index == middle_index:
                yield item
            else:
                yield item
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = middle_element_generator(data1)
    print("Data 1:")
    for element in gen1:
        print(element)
    data2 = [10, 20, 30, 40, 50, 60]
    gen2 = middle_element_generator(data2)
    print("\nData 2:")
    for element in gen2:
        print(element)
    data3 = [100]
    gen3 = middle_element_generator(data3)
    print("\nData 3:")
    for element in gen3:
        print(element)
    data4 = []
    gen4 = middle_element_generator(data4)
    print("\nData 4:")
    for element in gen4:
        print("No middle element")