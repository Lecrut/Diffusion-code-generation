def calculate_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_median(sample_array))