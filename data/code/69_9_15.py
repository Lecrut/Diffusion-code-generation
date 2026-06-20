def access_list_elements(lst, indices):
    return [lst[idx] if 0 <= idx < len(lst) else None for idx in indices]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 6]
    result = access_list_elements(sample_list, sample_indices)
    print(result)