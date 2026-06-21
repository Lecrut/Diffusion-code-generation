def get_final_item(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) == 0:
        raise ValueError("List is empty")
    return arr[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_final_item(sample_list))