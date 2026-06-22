def access_list_elements(lst, indices):
    def is_valid_index(index, length):
        return 0 <= index < length or (index < 0 and -index <= length)

    result = []
    for index in indices:
        if is_valid_index(index, len(lst)):
            result.append(lst[index])
    return result

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    sample_indices = [-1, -2, 0, 3, 5]
    print(access_list_elements(sample_list, sample_indices))