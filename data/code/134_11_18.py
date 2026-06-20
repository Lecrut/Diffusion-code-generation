def check_overlaps(tuples):
    sets = [set(t) for t in tuples]
    n = len(sets)
    for i in range(n):
        for j in range(i + 1, n):
            if not sets[i].isdisjoint(sets[j]):
                return True
    return False

if __name__ == '__main__':
    sample1 = (
        (1, 2),
        (3, 4),
        (5, 6)
    )
    print(f"Sample 1: {sample1}, Overlaps: {check_overlaps(sample1)}")

    sample2 = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    print(f"Sample 2: {sample2}, Overlaps: {check_overlaps(sample2)}")