def strictly_increasing_pairs(data):
    iterator = iter(data)
    try:
        previous = next(iterator)
    except StopIteration:
        return
    for current in iterator:
        if current > previous:
            yield True
        else:
            yield False
        previous = current
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(list1)
    print(list(strictly_increasing_pairs(list1)))
    list2 = [1, 3, 2, 4, 5]
    print(list2)
    print(list(strictly_increasing_pairs(list2)))
    list3 = [5, 4, 3, 2, 1]
    print(list3)
    print(list(strictly_increasing_pairs(list3)))
    list4 = [1, 1, 2, 3, 3]
    print(list4)
    print(list(strictly_increasing_pairs(list4)))
    list5 = [10, 20, 30]
    print(list5)
    print(list(strictly_increasing_pairs(list5)))
    list6 = []
    print(list6)
    print(list(strictly_increasing_pairs(list6)))