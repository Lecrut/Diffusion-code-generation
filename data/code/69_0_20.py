def access_elements(lst, *indices):
    return [lst[i] for i in indices if 0 <= i < len(lst)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_access = (0, 2, 4)
    result = access_elements(sample_list, *indices_to_access)
    print(result)