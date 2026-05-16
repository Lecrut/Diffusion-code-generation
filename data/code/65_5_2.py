def indexed_iterator(iterable, index):
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    try:
        if index < 0:
            return
        yield iterable[index]
    except IndexError:
        return
if __name__ == '__main__':
    data = list(range(1000000))
    print("Testing index 0:")
    for item in indexed_iterator(data, 0):
        print(item)
        if item == 1:
            break
    print("\nTesting index 500000:")
    for item in indexed_iterator(data, 500000):
        print(item)
        if item == 500000:
            break
    print("\nTesting out of bounds index (1000000):")
    for item in indexed_iterator(data, 1000000):
        print(item)
    print("\nTesting negative index (-1):")
    for item in indexed_iterator(data, -1):
        print(item)