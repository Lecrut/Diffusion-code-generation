def print_first_last(strings):
    if not strings:
        return None, None
    first = strings[0]
    last = strings[-1]
    return first, last

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['hello']
    list3 = []
    list4 = ['one', 'two']

    print(f"List 1: {print_first_last(list1)}")
    print(f"List 2: {print_first_last(list2)}")
    print(f"List 3: {print_first_last(list3)}")
    print(f"List 4: {print_first_last(list4)}")