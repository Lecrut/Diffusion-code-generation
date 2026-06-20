EXCLUSIVE_THRESHOLD = 0

def are_tuples_exclusive(tuples):
    sets = [set(tup) for tup in tuples]
    n = len(sets)
    for i in range(n):
        for j in range(i + 1, n):
            if not sets[i].isdisjoint(sets[j]):
                return False
    return True

if __name__ == '__main__':
    sample_tuples1 = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    print(f"Tuples 1: {sample_tuples1}, Exclusive: {are_tuples_exclusive(sample_tuples1)}")
    
    sample_tuples2 = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
    print(f"Tuples 2: {sample_tuples2}, Exclusive: {are_tuples_exclusive(sample_tuples2)}")