def is_valid_sequence(seq):
    if not isinstance(seq, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for item in seq:
        if not isinstance(item, int):
            raise ValueError("All elements in the sequence must be integers")

def total_recursive_memoization(seq, memo={}):
    is_valid_sequence(seq)
    if not seq:
        return 0
    if len(seq) in memo:
        return memo[len(seq)]
    result = seq[0] + total_recursive_memoization(seq[1:], memo)
    memo[len(seq)] = result
    return result

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(total_recursive_memoization(sample_sequence))