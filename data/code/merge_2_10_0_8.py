def sort_by_parity(arr):
    even_indices = []
    odd_indices = []
    for index in range(len(arr)):
        if arr[index] % 2 == 0:
            even_indices.append(index)
        else:
            odd_indices.append(index)
    sorted_arr = [arr[i] for i in odd_indices + even_indices]
    return sorted_arr
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 4, 7, 3, 6]
    if not isinstance(sample_list, list):
        raise TypeError("Input must be a list")
    sorted_result = sort_by_parity(sample_list)
    print(f"Sorted List: {sorted_result}")