def compare_lengths(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    yield (len1 < len2)
    yield (len1 > len2)
    yield (len1 == len2)
if __name__ == '__main__':
    seq1 = range(1000000)
    seq2 = range(500000)
    for result in compare_lengths(seq1, seq2):
        print(result)