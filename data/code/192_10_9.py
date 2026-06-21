def intersect(*lists):
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    result1 = intersect([1, 2, 3], [2, 3, 4], [3, 4, 5])
    print(result1)
    result2 = intersect([1, 2, 3, 4], [2, 3, 5, 6], [3, 4, 7, 8])
    print(result2)