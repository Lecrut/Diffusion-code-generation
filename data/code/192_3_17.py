def find_duplicates(*lists):
    sets = [set(lst) for lst in lists]
    intersection = set.intersection(*sets)
    return list(intersection)

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
        [5, 9, 10, 11, 12]
    ]
    duplicates = find_duplicates(*sample_lists)
    print(duplicates)