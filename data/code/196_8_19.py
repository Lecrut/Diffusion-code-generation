def extend_list(base, extension):
    base.extend(extension)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    extend_list(list1, list2)
    print(list1)