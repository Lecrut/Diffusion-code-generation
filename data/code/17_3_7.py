def last_element(collection):
    if isinstance(collection, (list, tuple)):
        return collection[-1]
    if isinstance(collection, str):
        return collection[-1]
    if hasattr(collection, '__getitem__'):
        try:
            return collection[-1]
        except IndexError:
            raise IndexError("Cannot get last element of an empty collection")
    if hasattr(collection, '__iter__'):
        last = None
        for item in collection:
            last = item
        if last is None:
            raise StopIteration("Cannot get last element of an empty iterator")
        return last
    raise TypeError("Unsupported collection type")

if __name__ == '__main__':
    print(last_element([1, 2, 3, 4, 5]))
    print(last_element((10, 20, 30)))
    print(last_element("hello"))
    print(last_element({1: 'a', 2: 'b', 3: 'c'}.keys()))