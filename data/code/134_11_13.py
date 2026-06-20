def check_overlap(tuples):
    sets = [set(t) for t in tuples]
    return any(s1.intersection(s2) for s1, s2 in combinations(sets, 2))

if __name__ == '__main__':
    sample_tuples1 = ((1, 2), (3, 4), (5, 6))
    print(f"Tuples 1: {sample_tuples1}, Overlapping: {check_overlap(sample_tuples1)}")
    sample_tuples2 = ((1, 2, 3), (4, 5), (6, 7))
    print(f"Tuples 2: {sample_tuples2}, Overlapping: {check_overlap(sample_tuples2)}")