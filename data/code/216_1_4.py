def find_middle_element(sorted_list):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == 0 or sorted_list[mid] > sorted_list[mid - 1]:
            return sorted_list[mid]
        elif mid < len(sorted_list) - 1 and sorted_list[mid] > sorted_list[mid + 1]:
            return sorted_list[mid]
        elif sorted_list[mid] < sorted_list[left]:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == '__main__':
    sample_list = [3, 5, 7, 8, 9, 10, 12]
    print(find_middle_element(sample_list))