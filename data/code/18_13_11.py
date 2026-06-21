def get_central_element(arr):
    if not arr:
        raise ValueError("Array is empty")
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [1, 2, 3, 4, 5, 6]
    print(get_central_element(sample_odd))
    print(get_central_element(sample_even))