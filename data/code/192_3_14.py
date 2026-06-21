def find_common_elements(*lists):
    sets = [set(lst) for lst in lists]
    common_elements = set.intersection(*sets)
    return list(common_elements)

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [4, 5, 7, 8]
    ]
    duplicates = find_common_elements(*sample_lists)
    print(duplicates)