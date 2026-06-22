def calculate_median(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2.0
    else:
        return arr[mid]

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2]
    print(calculate_median(sample_array))