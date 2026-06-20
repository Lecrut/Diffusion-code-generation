def find_first_true(sequence):
    return any(item for item in sequence)

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    result1 = find_first_true(seq1)
    print(f"Sequence: {seq1}, First True found: {result1}")
    
    seq2 = [False, False, False]
    result2 = find_first_true(seq2)
    print(f"Sequence: {seq2}, First True found: {result2}")
    
    seq3 = [True, False, False]
    result3 = find_first_true(seq3)
    print(f"Sequence: {seq3}, First True found: {result3}")