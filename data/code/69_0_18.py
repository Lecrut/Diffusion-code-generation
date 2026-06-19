def access_elements(lst, *indices):
    result = []
    for index in indices:
        try:
            result.append(lst[index])
        except IndexError:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, -1, 5, -3)
    accessed_elements = access_elements(sample_list, *indices_to_access)
    print(accessed_elements)