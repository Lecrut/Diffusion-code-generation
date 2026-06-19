def compare_lengths(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 < len2:
        yield (-1)
    elif len1 > len2:
        yield 1
    else:
        yield 0
if __name__ == '__main__':
    sequence1 = range(1000000)
    sequence2 = range(500000)
    comparison_result = next(compare_lengths(sequence1, sequence2))
    print(comparison_result)