def sum_differs(list1, list2):
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    print(sum_differs(list1, list2))