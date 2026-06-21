def find_middle_element(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < lst[right]:
            right = mid
        else:
            left = mid + 1
    return lst[left]

if __name__ == '__main__':
    sample_list = [3, 5, 7, 8, 9, 10]
    print(find_middle_element(sample_list))