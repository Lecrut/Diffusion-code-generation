def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 2.7]
    bubble_sort(sample_values)
    print(sample_values)