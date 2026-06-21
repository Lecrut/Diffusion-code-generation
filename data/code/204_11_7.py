def find_middle_element(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[mid + 1]:
            return lst[mid]
        elif lst[mid] < lst[mid - 1]:
            return lst[mid - 1]
        elif lst[mid] > lst[left]:
            left = mid + 1
        else:
            right = mid - 1
    return lst[left]

if __name__ == '__main__':
    sample_list = [3, 4, 5, 1, 2]
    print(find_middle_element(sample_list))