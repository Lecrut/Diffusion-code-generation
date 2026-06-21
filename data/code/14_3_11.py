def third_element(iterable):
    iterator = iter(iterable)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    print(third_element([1, 2, 3, 4, 5]))
    print(third_element("hello"))
    print(third_element((x for x in range(10))))
    print(third_element([1, 2]))