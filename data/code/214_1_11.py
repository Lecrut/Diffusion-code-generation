def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_array = [34, 78, 12, 56, 90, 23, 45]
    print(find_smallest(sample_array))