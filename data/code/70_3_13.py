def get_first_last(iterable):
    return (iterable[0], iterable[-1]) if iterable else (None, None)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b']
    list3 = []
    print(f"List 1: {get_first_last(list1)}")
    print(f"List 2: {get_first_last(list2)}")
    print(f"List 3: {get_first_last(list3)}")