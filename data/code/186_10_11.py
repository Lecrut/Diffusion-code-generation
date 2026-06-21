def timsort(arr):
    min_run = 32

    def insertion_sort(left, right):
        for i in range(left + 1, right + 1):
            key_item = arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item

    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + size * 2 - 1), (n - 1))
            merged_array = arr[left:mid+1] + arr[mid+1:right+1]
            arr[left:left+len(merged_array)] = sorted(merged_array)

        size *= 2

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    timsort(sample_list)
    print(sample_list)