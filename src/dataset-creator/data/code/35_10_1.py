def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
if __name__ == '__main__':
    sample_data = [2, 5, 8, 10, 13, 17, 20]
    print(binary_search(sample_data, 10))
    print(binary_search([], 10))
    print(binary_search([1], 5))