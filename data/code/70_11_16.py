def print_first_last(strings):
    if not strings:
        return
    first = strings[0]
    last = strings[-1]
    print(first, last)

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['red']
    list3 = []
    list4 = ['hello', 'world']

    print_first_last(list1)
    print_first_last(list2)
    print_first_last(list3)
    print_first_last(list4)