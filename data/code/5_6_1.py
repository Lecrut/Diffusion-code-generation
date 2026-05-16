def compare_lengths_generator(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    yield len1
    yield len2
if __name__ == '__main__':
    sequence_a = list(range(1000000))
    sequence_b = list(range(500000))
    print("Comparing lengths of sequence_a and sequence_b:")
    for length in compare_lengths_generator(sequence_a, sequence_b):
        print(length)