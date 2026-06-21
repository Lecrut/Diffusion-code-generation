def get_third_element(iterable):
    iterator = iter(iterable)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    data = [10, 20, 30, 40]
    print(get_third_element(data))
    print(get_third_element((1, 2, 3)))
    print(get_third_element(iter('abc')))
    print(get_third_element([]))