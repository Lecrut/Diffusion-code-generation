def access_list_elements(lst, indices):
    return [lst[index] for index in indices if 0 <= index < len(lst)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 6]
    print(access_list_elements(sample_list, sample_indices))