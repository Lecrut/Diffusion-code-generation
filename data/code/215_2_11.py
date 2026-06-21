def find_largest_integer(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_array = [100, 200, 50, 300, 75]
    print(find_largest_integer(sample_array))