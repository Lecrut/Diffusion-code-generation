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
    if 'last_element' in locals():
        yield last_element
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    print("Data 1:")
    for element in last_element_generator(data1):
        print(element)
    data2 = [100]
    print("\nData 2:")
    for element in last_element_generator(data2):
        print(element)
    data3 = []
    print("\nData 3:")
    for element in last_element_generator(data3):
        print(element)
    data4 = [99]
    print("\nData 4:")
    for element in last_element_generator(data4):
        print(element)
    data5 = [1, 2, 3]
    print("\nData 5:")
    for element in last_element_generator(data5):
        print(element)