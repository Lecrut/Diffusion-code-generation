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
    large_seq1 = range(10 ** 6)
    large_seq2 = range(10 ** 7)
    comparison_result = next(compare_lengths(large_seq1, large_seq2))
    print(comparison_result)