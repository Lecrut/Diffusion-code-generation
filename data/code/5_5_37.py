def compare_lengths(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 < len2:
        yield -1
    elif len1 > len2:
        yield 1
    else:
        yield 0

if __name__ == '__main__':
    sequence_a = range(2000000)
    sequence_b = range(1500000)
    comparison_result = next(compare_lengths(sequence_a, sequence_b))
    print(comparison_result)