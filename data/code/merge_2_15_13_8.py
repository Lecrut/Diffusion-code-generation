import sys
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    sorted_arr = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    return sorted_arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    return arr
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def main():
    dataset_integers = [64, 34, 25, 12, 22, 11, 90, 88, 76, 55, 44, 33, 22, 11]
    test_cases = {
        "Quick Sort": quick_sort(dataset_integers.copy()),
        "Merge Sort": merge_sort(dataset_integers.copy()),
        "Bubble Sort": bubble_sort(dataset_integers.copy()),
        "Selection Sort": selection_sort(dataset_integers.copy())
    }
    for algorithm, result in test_cases.items():
        print(f"{algorithm}: {result}")
if __name__ == '__main__':
    main()