def last_element(collection):
    if not collection:
        raise IndexError("Collection is empty")
    if hasattr(collection, '__getitem__') and hasattr(collection, '__len__'):
        return collection[-1]
    if hasattr(collection, '__iter__'):
        iterator = iter(collection)
        try:
            prev = next(iterator)
            while True:
                prev = next(iterator)
            return prev
        except StopIteration:
            return prev
    raise TypeError("Unsupported collection type")

if __name__ == '__main__':
    print(last_element([1, 2, 3, 4, 5]))
    print(last_element("hello"))
    print(last_element((10, 20, 30)))
    print(last_element(x * 2 for x in range(5)))