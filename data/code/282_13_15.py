def total_recursive_memoization(seq, memo={}):
    if not isinstance(seq, list) or not all(isinstance(x, int) for x in seq):
        raise ValueError("Input must be a list of integers")
    if not seq:
        return 0
    if len(seq) in memo:
        return memo[len(seq)]
    result = seq[0] + total_recursive_memoization(seq[1:], memo)
    memo[len(seq)] = result
    return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    try:
        print(total_recursive_memoization(sample_sequence))
    except ValueError as e:
        print(e)