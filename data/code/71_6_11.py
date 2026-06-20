def find_median(data):
    n = len(data)
    if n == 0:
        return None
    else:
        sorted_data = sorted(data)
        middle_index = n // 2
        if n % 2 == 1:
            return sorted_data[middle_index]
        else:
            lower_middle_index = middle_index - 1
            return (sorted_data[lower_middle_index] + sorted_data[middle_index]) / 2
if __name__ == '__main__':
    list1 = [4, 5, 3, 8, 1, 9]
    list2 = [20, 30, 10, 40]
    list3 = [7, 2, 5, 1, 8, 3, 6]
    list4 = [1, 2, 3, 4, 5]
    list5 = [100]
    print(find_median(list1))
    print(find_median(list2))
    print(find_median(list3))
    print(find_median(list4))
    print(find_median(list5))