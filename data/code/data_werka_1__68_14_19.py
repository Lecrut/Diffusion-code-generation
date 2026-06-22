def symmetric_difference(iterable1: set, iterable2: set) -> set:
    if not isinstance(iterable1, set) or not isinstance(iterable2, set):
        raise TypeError("Both inputs must be sets")
    return iterable1 ^ iterable2

if __name__ == '__main__':
    set_a = {1, 3, 5, 7}
    set_b = {3, 4, 5, 6}
    result = symmetric_difference(set_a, set_b)
    print(result)