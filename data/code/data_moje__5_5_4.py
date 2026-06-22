def compare_lengths_generator(seq1, seq2):
    yield len(seq1) > len(seq2)
    yield len(seq1) < len(seq2)
    yield len(seq1) == len(seq2)

if __name__ == '__main__':
    sample1 = range(1000000)
    sample2 = range(500000)
    results = list(compare_lengths_generator(sample1, sample2))
    print(results)