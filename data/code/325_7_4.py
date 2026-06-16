def compare_pairs(seq1, seq2):
    for a in seq1:
        for b in seq2:
            yield (a, b)
if __name__ == '__main__':
    sequence1 = [1, 2, 3]
    sequence2 = [4, 5, 6]
    results = list(compare_pairs(sequence1, sequence2))
    for pair in results:
        print(pair)