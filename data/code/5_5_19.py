def compare_lengths_generator(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 < len2:
        yield 'shorter'
    elif len1 > len2:
        yield 'longer'
    else:
        yield 'equal'

if __name__ == '__main__':
    sample_seq1 = [1, 2, 3, 4, 5]
    sample_seq2 = [10, 20, 30]
    for result in compare_lengths_generator(sample_seq1, sample_seq2):
        print(result)
    sample_seq3 = [1, 2]
    sample_seq4 = [1, 2]
    for result in compare_lengths_generator(sample_seq3, sample_seq4):
        print(result)
    sample_seq5 = [1]
    sample_seq6 = [1, 2, 3]
    for result in compare_lengths_generator(sample_seq5, sample_seq6):
        print(result)