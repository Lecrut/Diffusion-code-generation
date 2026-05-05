def get_first_and_last(iterable):
    try:
        return iterable[0], iterable[-1]
    except IndexError:
        return None, None
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b']
    list3 = []
    list4 = [10]
    print(f"List 1: {get_first_and_last(list1)}")
    print(f"List 2: {get_first_and_last(list2)}")
    print(f"List 3: {get_first_and_last(list3)}")
    print(f"List 4: {get_first_and_last(list4)}")