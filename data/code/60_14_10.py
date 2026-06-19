def get_final_item(arr):
    if not arr:
        raise ValueError("Array is empty")
    return arr[-1]

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    print(get_final_item(sample_array))