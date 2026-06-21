def find_kth_smallest(arr, k):
    if not arr or k <= 0:
        raise ValueError("Array must be non-empty and k must be positive.")
    if k > len(arr):
        raise ValueError("k is larger than the length of the array.")

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[store_index], arr[right] = arr[right], arr[store_index]
        return store_index

    left, right = 0, len(arr) - 1
    while True:
        pivot_index = left + (right - left) // 2
        pivot_index = partition(left, right, pivot_index)
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index < k - 1:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

if __name__ == '__main__':
    sample_numbers = [3, 2, 9, 0, 5, 6]
    k = 4
    try:
        result = find_kth_smallest(sample_numbers, k)
        print(f"The {k}-th smallest element is: {result}")
    except ValueError as e:
        print(e)