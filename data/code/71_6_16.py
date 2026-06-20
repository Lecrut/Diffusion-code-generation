def find_median(data):
    if not data:
        raise ValueError('The list is empty')
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        lower_middle_index = n // 2 - 1
        return sorted_data[lower_middle_index]
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [10, 4, 7, 2, 9]
    list3 = [1, 2, 3, 4]
    list4 = [1, 2, 3, 4, 5]
    list5 = [1, 2, 3, 4, 5, 6]
    print(find_median(list1))
    print(find_median(list2))
    print(find_median(list3))
    print(find_median(list4))
    print(find_median(list5))