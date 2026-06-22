def total_recursive_memoization(seq, memo={}):
    if not seq:
        return 0
    if len(seq) in memo:
        return memo[len(seq)]
    result = seq[-1] + total_recursive_memoization(seq[:-1], memo)
    memo[len(seq)] = result
    return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(total_recursive_memoization(sample_sequence))