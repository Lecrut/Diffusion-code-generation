def compare_elements(list1, list2, index):
    try:
        return (list1[index], list2[index])
    except IndexError:
        return (None, None)
if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = ['a', 'b', 'c', 'd', 'e']
    index = 2
    print(compare_elements(list1, list2, index))
    index = 5
    print(compare_elements(list1, list2, index))