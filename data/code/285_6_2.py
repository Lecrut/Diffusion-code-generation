def check_adjacent_increasing(arr):
    n = len(arr)
    if n < 2:
        return True
    for i in range(n - 1):
        if arr[i] >= arr[i+1]:
            return False
    return True
if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    print(check_adjacent_increasing(array1))
    array2 = [1, 3, 2, 4]
    print(check_adjacent_increasing(array2))
    array3 = [5, 4, 3, 2, 1]
    print(check_adjacent_increasing(array3))
    array4 = [10, 20, 30]
    print(check_adjacent_increasing(array4))
    array5 = [1, 1, 2]
    print(check_adjacent_increasing(array5))
    array6 = []
    print(check_adjacent_increasing(array6))