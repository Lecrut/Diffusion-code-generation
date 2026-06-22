def get_third_element(sequence):
    iterator = iter(sequence)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    print(get_third_element([1, 2, 3, 4, 5]))
    print(get_third_element((10, 20, 30)))
    print(get_third_element("hello"))
    print(get_third_element([1, 2]))
    print(get_third_element(()))