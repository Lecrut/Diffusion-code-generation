import sys
def append_to_immutable(seq):
    new_seq = seq + (seq[-1],) if len(seq) > 0 else tuple()
    return new_seq
if __name__ == '__main__':
    sample_data = (1, 2, 3)
    result = append_to_immutable(sample_data)
    print(result)