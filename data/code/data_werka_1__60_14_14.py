def get_last_item(arr):
    if not arr:
        raise ValueError("Array is empty")
    return arr[-1]

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    print(get_last_item(sample_array))