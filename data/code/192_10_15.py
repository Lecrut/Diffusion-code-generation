def intersect(*lists):
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    sample_lists = ([1, 2, 3], [2, 3, 4], [3, 4, 5])
    result = intersect(*sample_lists)
    print(result)