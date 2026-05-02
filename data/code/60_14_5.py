def last_element_generator(iterable):
    it = iter(iterable)
    last_element = None
    try:
        last_element = next(it)
    except StopIteration:
        return
    for element in it:
        last_element = element
        yield last_element
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    print("Data 1:")
    for item in last_element_generator(data1):
        print(item)
    data2 = [100, 200, 300]
    print("\nData 2:")
    for item in last_element_generator(data2):
        print(item)
    data3 = [42]
    print("\nData 3:")
    for item in last_element_generator(data3):
        print(item)
    data4 = []
    print("\nData 4 (Empty):")
    try:
        for item in last_element_generator(data4):
            print(item)
    except StopIteration:
        pass