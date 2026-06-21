def intersect(*lists):
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        [2, 3, 5, 6],
        [3, 4, 7, 8]
    ]
    result = intersect(*sample_lists)
    print(result)