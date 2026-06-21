list1 = [1, 2, 3]
list2 = [4, 5, 6]

def concatenate_lists(l1, l2):
    l1.extend(l2)
    return l1

if __name__ == '__main__':
    result = concatenate_lists(list1, list2)
    print(result)