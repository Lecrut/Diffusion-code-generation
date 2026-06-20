def are_tuples_disjoint(tuples):
    sets = [set(t) for t in tuples]
    return all(not s1.intersection(s2) for s1, s2 in ((sets[i], sets[j]) for i in range(len(sets)) for j in range(i + 1, len(sets))))

if __name__ == '__main__':
    print(are_tuples_disjoint([(1, 2), (3, 4), (5, 6)]))
    print(are_tuples_disjoint([(1, 2, 3), (3, 4), (5, 6)]))