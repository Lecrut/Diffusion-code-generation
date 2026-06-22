def total_recursive_memoization(seq, memo={}):
    if len(seq) == 0:
        return 0
    if seq[0] in memo:
        return memo[seq[0]] + total_recursive_memoization(seq[1:], memo)
    else:
        result = seq[0] + total_recursive_memoization(seq[1:], memo)
        memo[seq[0]] = result
        return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(total_recursive_memoization(sample_sequence))