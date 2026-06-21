def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6]
    selection_sort(sample_values)
    print(sample_values)