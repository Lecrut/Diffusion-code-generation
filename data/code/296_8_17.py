def find_pairs_with_ratio(start, end, target_ratio):
    if start > end:
        raise ValueError("Start of range must be less than or equal to end.")
    if target_ratio <= 0:
        raise ValueError("Target ratio must be positive.")

    pairs = []
    for a in range(start, end + 1):
        b = a * target_ratio
        if b.is_integer() and start <= int(b) <= end:
            pairs.append((a, int(b)))
    return pairs

if __name__ == '__main__':
    sample_start = 1
    sample_end = 20
    sample_target_ratio = 2.5
    print(find_pairs_with_ratio(sample_start, sample_end, sample_target_ratio))