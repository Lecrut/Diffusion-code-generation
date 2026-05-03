def last_element_generator(iterable):
    it = iter(iterable)
    try:
        last_element = next(it)
    except StopIteration:
        return
    while True:
        try:
            last_element = next(it)
        except StopIteration:
            yield last_element
            return
    if __name__ == '__main__':
        data1 = [1, 2, 3, 4, 5]
        print("Last element of data1:", next(last_element_generator(data1)))
        data2 = [100]
        print("Last element of data2:", next(last_element_generator(data2)))
        data3 = []
        print("Last element of data3:", end="None")
        try:
            next(last_element_generator(data3))
        except StopIteration:
            print("None")