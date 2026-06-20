def has_overlapping_elements(tuples):
    sets = [set(tup) for tup in tuples]
    n = len(sets)
    for i in range(n):
        for j in range(i + 1, n):
            if not sets[i].isdisjoint(sets[j]):
                return True
    return False

if __name__ == '__main__':
    sample_input1 = (
        (1, 2),
        (3, 4),
        (5, 6)
    )
    print(f"Sample Input 1: {sample_input1}, Overlapping Elements: {has_overlapping_elements(sample_input1)}")
    
    sample_input2 = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    print(f"Sample Input 2: {sample_input2}, Overlapping Elements: {has_overlapping_elements(sample_input2)}")