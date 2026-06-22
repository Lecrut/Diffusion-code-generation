def access_elements(lst, *indices):
    index_map = {i: lst[i] if 0 <= i < len(lst) else None for i in indices}
    return [index_map[i] for i in indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, 4, -1, -3, 5, -6)
    result = access_elements(sample_list, *indices_to_access)
    print(result)