def symmetric_difference(iterable1, iterable2):
    set1 = set(iterable1)
    set2 = set(iterable2)
    return list(set1.symmetric_difference(set2))

if __name__ == '__main__':
    list_a = [1, 3, 5, 7]
    list_b = [3, 4, 5, 6]
    result = symmetric_difference(list_a, list_b)
    print(result)