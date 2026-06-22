def get_central_element(arr):
    if not arr:
        raise ValueError("Array must not be empty")
    index = len(arr) // 2
    return arr[index]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [1, 2, 3, 4, 5, 6]
    print(get_central_element(sample_odd))
    print(get_central_element(sample_even))