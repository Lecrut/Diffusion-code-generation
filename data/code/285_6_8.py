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
    array3 = [5, 4, 3, 2, 1]
    array4 = [10, 20, 30]
    array5 = [1, 1, 2]
    array6 = [7, 7, 8]
    array7 = []
    array8 = [5]
    print(f"Array {array1}: {check_adjacent_increasing(array1)}")
    print(f"Array {array2}: {check_adjacent_increasing(array2)}")
    print(f"Array {array3}: {check_adjacent_increasing(array3)}")
    print(f"Array {array4}: {check_adjacent_increasing(array4)}")
    print(f"Array {array5}: {check_adjacent_increasing(array5)}")
    print(f"Array {array6}: {check_adjacent_increasing(array6)}")
    print(f"Array {array7}: {check_adjacent_increasing(array7)}")
    print(f"Array {array8}: {check_adjacent_increasing(array8)}")