def find_common_elements(*lists):
    sets = [set(lst) for lst in lists]
    common_elements = set.intersection(*sets)
    return list(common_elements)

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40],
        [30, 40, 50, 60],
        [40, 50, 70, 80]
    ]
    common_elements = find_common_elements(*sample_lists)
    print(common_elements)