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
    array2 = [1, 3, 2, 4]
    array3 = [10, 20, 30]
    array4 = [5, 5, 6]
    array5 = [1, 2, 2, 4]
    array6 = [7]
    print(f"Array {array1}: {check_adjacent_increasing(array1)}")
    print(f"Array {array2}: {check_adjacent_increasing(array2)}")
    print(f"Array {array3}: {check_adjacent_increasing(array3)}")
    print(f"Array {array4}: {check_adjacent_increasing(array4)}")
    print(f"Array {array5}: {check_adjacent_increasing(array5)}")
    print(f"Array {array6}: {check_adjacent_increasing(array6)}")