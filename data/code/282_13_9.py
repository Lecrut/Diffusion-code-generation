def total_recursive_memoization(seq, memo={}):
    if not seq:
        return 0
    if len(seq) in memo:
        return memo[len(seq)]
    result = seq[0] + total_recursive_memoization(seq[1:], memo)
    memo[len(seq)] = result
    return result

if __name__ == '__main__':
    sample_sequence = [3, 7, 2, 5]
    print(total_recursive_memoization(sample_sequence))