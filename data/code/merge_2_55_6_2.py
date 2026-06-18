def swap_consecutive(seq):
    if len(seq) < 2:
        return seq
    try:
        seq[0], seq[-2] = seq[-2], seq[0]
        return seq
    except (IndexError, TypeError):
        pass
    if len(seq) < 3:
        return list(seq)
def swap_consecutive_indices(seq):
    try:
        seq[0], seq[-2] = seq[-2], seq[0]
        return seq
    except (IndexError, TypeError):
        pass
    if len(seq) < 3:
        return list(seq)
if __name__ == '__main__':
    test_list = [10, 20, 30, 40]
    result = swap_consecutive_indices(test_list)
    print(result)