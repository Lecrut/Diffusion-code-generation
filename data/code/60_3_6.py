def get_last_element(arr):
    if not isinstance(arr, (list, tuple)):
        raise TypeError("Input must be a list or a tuple")
    if len(arr) == 0:
        raise ValueError("Array cannot be empty")
    return arr[-1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(get_last_element(sample_list))