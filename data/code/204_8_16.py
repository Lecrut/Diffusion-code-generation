def find_middle_element(arr):
    n = len(arr)
    if n == 0:
        return None
    middle_index = n // 2
    return arr[middle_index]

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    print(find_middle_element(sample_array))