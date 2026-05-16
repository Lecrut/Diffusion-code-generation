def length_comparator_generator(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    yield len1
    yield len2
if __name__ == '__main__':
    sequence_a = list(range(1000000))
    sequence_b = list(range(500000))
    comparator = length_comparator_generator(sequence_a, sequence_b)
    results = []
    for length in comparator:
        results.append(length)
    print(results)