def find_middle_element(arr):
    if not arr:
        return None
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    print(find_middle_element(sample_array))