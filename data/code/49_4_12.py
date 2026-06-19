def compute_ratio(length1, length2):
    min_length = min(length1, length2)
    max_length = max(length1, length2)
    if min_length == 0:
        return float('inf')
    return max_length / min_length

if __name__ == '__main__':
    len_a = 7
    len_b = 28
    ratio = compute_ratio(len_a, len_b)
    print(ratio)