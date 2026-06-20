def compare_length_generator(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 < len2:
        yield 'seq1 is shorter than seq2'
    elif len1 > len2:
        yield 'seq1 is longer than seq2'
    else:
        yield 'seq1 and seq2 have equal length'

if __name__ == '__main__':
    sample_seq1 = list(range(10))
    sample_seq2 = tuple(range(10, 20))
    sample_seq3 = list(range(100))
    
    result_gen1 = compare_length_generator(sample_seq1, sample_seq2)
    print(next(result_gen1))
    
    result_gen2 = compare_length_generator(sample_seq1, sample_seq3)
    print(next(result_gen2))
    
    result_gen3 = compare_length_generator(sample_seq1, sample_seq1)
    print(next(result_gen3))