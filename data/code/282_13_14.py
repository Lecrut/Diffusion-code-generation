def total_recursive_memoized(seq, memo={}):
    if not seq:
        return 0
    if seq[0] in memo:
        return memo[seq[0]] + total_recursive_memoized(seq[1:], memo)
    else:
        result = seq[0] + total_recursive_memoized(seq[1:], memo)
        memo[seq[0]] = result
        return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(total_recursive_memoized(sample_sequence))