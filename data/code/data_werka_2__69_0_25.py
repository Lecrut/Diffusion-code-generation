def access_elements(lst, *indices):
    index_map = {index: lst[index] if 0 <= index < len(lst) else None for index in indices}
    return [index_map[index] for index in indices]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    indices_to_access = (1, -2, 4, 5, -6)
    result = access_elements(sample_list, *indices_to_access)
    print(result)