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
    sample_seq1 = range(1000000)
    sample_seq2 = range(500000)
    for result in compare_lengths(sample_seq1, sample_seq2):
        print(result)