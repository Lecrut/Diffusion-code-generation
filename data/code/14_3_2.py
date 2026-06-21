def third_element(iterable):
    try:
        return iterable[2]
    except TypeError:
        for i, item in enumerate(iterable):
            if i == 2:
                return item
        raise IndexError("Iterable does not have a third element")

if __name__ == '__main__':
    print(third_element([1, 2, 3, 4, 5]))
    print(third_element("hello"))
    print(third_element((x for x in range(10))))
    try:
        print(third_element([1, 2]))
    except IndexError as e:
        print(repr(e))