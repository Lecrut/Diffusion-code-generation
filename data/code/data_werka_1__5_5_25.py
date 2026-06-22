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
    seq1 = range(10 ** 6)
    seq2 = range(10 ** 6 + 1)
    result = list(compare_lengths(seq1, seq2))
    print(result)