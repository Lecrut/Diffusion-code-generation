def get_first_last(iterable):
    try:
        return iterable[0], iterable[-1]
    except IndexError:
        return None, None
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10]
    list3 = []
    print(get_first_last(list1))
    print(get_first_last(list2))
    print(get_first_last(list3))