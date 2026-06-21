def range_of_sequence(seq):
    if not seq:
        return None
    return max(seq) - min(seq)
if __name__ == '__main__':
    sample_seq = [3.5, 1.2, 7.8, 0.9]
    print(range_of_sequence(sample_seq))