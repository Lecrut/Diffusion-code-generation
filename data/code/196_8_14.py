def extend_list(base, to_add):
    base.extend(to_add)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    extend_list(list1, list2)
    print(list1)