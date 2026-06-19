def access_elements(lst, *indices):
    return [lst[i] for i in indices]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = access_elements(sample_list, 0, 2, 4)
    print(result)