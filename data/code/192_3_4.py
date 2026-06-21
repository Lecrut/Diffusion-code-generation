def find_duplicates(*lists):
    sets = [set(lst) for lst in lists]
    intersection = set.intersection(*sets)
    return list(intersection)

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        [2, 3, 5, 6],
        [3, 4, 7, 8]
    ]
    print(find_duplicates(*sample_lists))