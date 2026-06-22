def find_middle(arr):
    n = len(arr)
    middle_index = (n - 1) // 2
    middle_value = arr[middle_index]
    return middle_index, middle_value

if __name__ == '__main__':
    indices, values = find_middle([1, 2, 3, 4, 5]), find_middle([1, 2, 3, 4, 5, 6])
    print(indices, values)
    indices2, values2 = find_middle([10, 20, 30]), find_middle([7])
    print(indices2, values2)