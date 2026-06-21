def intersect(*lists):
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    result1 = intersect([1, 2, 3], [2, 3, 4], [3, 4, 5])
    print(result1)
    result2 = intersect([10, 20, 30, 40], [30, 40, 50, 60], [40, 50, 70, 80])
    print(result2)