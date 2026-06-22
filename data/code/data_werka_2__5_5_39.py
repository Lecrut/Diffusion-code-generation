def compare_lengths(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    
    if len1 < len2:
        return (-1)
    elif len1 > len2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sequence_a = range(1500000)
    sequence_b = range(750000)
    result = compare_lengths(sequence_a, sequence_b)
    print(result)