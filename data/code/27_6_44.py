def sum_lists_differ(list1, list2):
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8]
    result = sum_lists_differ(list1, list2)
    print(result)