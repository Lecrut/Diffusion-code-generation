def find_smallest(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_smallest(sample_array))