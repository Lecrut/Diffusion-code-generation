def access_elements(lst, *indices):
    return [lst[i] for i in indices]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    indices_to_access = (0, 2, -1)
    accessed_elements = access_elements(sample_list, *indices_to_access)
    print(accessed_elements)