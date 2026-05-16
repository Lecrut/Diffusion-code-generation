def indexed_generator(iterable, index):
    for item in iterable:
        if index == 0:
            yield item
        elif index == 1:
            yield item
        else:
            continue
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print("Index 0:")
    for item in indexed_generator(data, 0):
        print(item)
    print("\nIndex 1:")
    for item in indexed_generator(data, 1):
        print(item)
    print("\nIndex 2:")
    for item in indexed_generator(data, 2):
        print(item)
    print("\nIndex 5 (out of bounds):")
    for item in indexed_generator(data, 5):
        print(item)