def intersect(*lists):
    sets = map(set, lists)
    common_elements = set.intersection(*sets)
    return sorted(common_elements)

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40],
        [30, 40, 50, 60],
        [40, 50, 70, 80]
    ]
    result = intersect(*sample_lists)
    print(result)