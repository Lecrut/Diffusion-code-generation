def total_sequence(seq, memo={}):
    if not seq:
        return 0
    if len(seq) in memo:
        return memo[len(seq)]
    result = seq[0] + total_sequence(seq[1:], memo)
    memo[len(seq)] = result
    return result
if __name__ == '__main__':
    sample_seq = [1, 2, 3, 4, 5]
    print(total_sequence(sample_seq))