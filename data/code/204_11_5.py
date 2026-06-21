def find_middle_element(lst):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == 0 or lst[mid] > lst[mid - 1]:
            return lst[mid]
        elif mid == len(lst) - 1 or lst[mid] < lst[mid + 1]:
            return lst[mid]
        elif lst[mid] < lst[left]:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == '__main__':
    sample_list = [3, 5, 7, 8, 9, 10, 20]
    print(find_middle_element(sample_list))