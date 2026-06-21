def find_kth_smallest(arr, k):
    if k <= 0 or k > len(arr):
        return None
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k <= len(left):
        return find_kth_smallest(left, k)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return find_kth_smallest(right, k - len(left) - len(middle))
if __name__ == '__main__':
    print(find_kth_smallest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_smallest([7, 10, 4, 3, 20, 15], 3))