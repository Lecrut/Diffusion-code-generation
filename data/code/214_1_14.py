def find_smallest(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_array = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_smallest(sample_array))