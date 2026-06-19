def compare_lengths(seq1, seq2):
    for item1 in seq1:
        for item2 in seq2:
            yield len(item1) == len(item2)

if __name__ == '__main__':
    sample_seq1 = ["apple", "banana", "cherry"]
    sample_seq2 = ["dog", "elephant", "frog"]

    comparison_results = compare_lengths(sample_seq1, sample_seq2)
    for result in comparison_results:
        print(result)