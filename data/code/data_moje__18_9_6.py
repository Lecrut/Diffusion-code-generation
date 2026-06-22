def get_median_via_division(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    if n == 0:
        return None
    mid_index = (n - 1) // 2
    if n % 2 == 0:
        left_index = mid_index - 1
        if left_index < 0:
            left_index = 0
        median = (sorted_list[left_index] + sorted_list[mid_index]) / 2.0
    else:
        median = sorted_list[mid_index]
    return median

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [10, 20, 30, 40]
    list3 = [7]
    
    print(get_median_via_division(list1))
    print(get_median_via_division(list2))
    print(get_median_via_division(list3))