def total_with_memoization(sequence, memo={}):
    if len(sequence) == 0:
        return 0
    if sequence in memo:
        return memo[sequence]
    result = sequence[0] + total_with_memoization(sequence[1:], memo)
    memo[sequence] = result
    return result

if __name__ == '__main__':
    sample_sequence = (3, 5, 7, 9)
    print(total_with_memoization(sample_sequence))