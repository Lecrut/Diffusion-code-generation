def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    middle_index = n // 2
    return sorted_data[middle_index] if n % 2 != 0 else sorted_data[middle_index - 1]
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