def get_last_element(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        raise ValueError("Input must be a non-empty list")
    return arr[-1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(get_last_element(sample_list))