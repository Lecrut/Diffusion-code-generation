def get_median(lst):
    sorted_list = sorted(lst)
    length = len(sorted_list)
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) // 2
    return sorted_list[mid_index]

if __name__ == '__main__':
    nums1 = [3, 1, 4, 1, 5]
    nums2 = [10, 20, 30, 40]
    print(get_median(nums1))
    print(get_median(nums2))