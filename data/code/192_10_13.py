def intersect(*lists):
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    result = intersect([1, 2, 3, 4], [2, 3, 5, 6], [3, 4, 7, 8])
    print(result)