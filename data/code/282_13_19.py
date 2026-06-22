def total_recursive_memoization(seq, memo={}):
    if not seq:
        return 0
    if len(seq) not in memo:
        memo[len(seq)] = seq[-1] + total_recursive_memoation(seq[:-1], memo)
    return memo[len(seq)]

if __name__ == '__main__':
    sample_sequence = [4, 3, 2, 1]
    print(total_recursive_memoization(sample_sequence))