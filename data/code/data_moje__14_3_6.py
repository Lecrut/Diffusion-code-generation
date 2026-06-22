def third_element(iterable):
    it = iter(iterable)
    try:
        next(it)
        next(it)
        return next(it)
    except StopIteration:
        raise IndexError("Iterable does not have a third element")

if __name__ == '__main__':
    print(third_element([1, 2, 3, 4, 5]))
    print(third_element("hello"))
    print(third_element((x for x in range(10))))