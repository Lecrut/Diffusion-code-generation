def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_array = [3, 5, 1, 2, 4, 8, 6, 7]
    print(find_largest(sample_array))