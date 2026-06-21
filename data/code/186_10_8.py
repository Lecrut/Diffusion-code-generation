def timsort(arr):
    if len(arr) <= 32:
        return insertion_sort(arr)
    mid = len(arr) // 2
    left, right = timsort(arr[:mid]), timsort(arr[mid:])
    return merge(left, right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == '__main__':
    sample = [34, 7, 23, 32, 5, 62]
    print(timsort(sample))