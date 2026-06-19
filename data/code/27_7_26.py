def sum_lists_differ(list1, list2):
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [6, 7, 8, 9]
    result = sum_lists_differ(list_a, list_b)
    print(result)