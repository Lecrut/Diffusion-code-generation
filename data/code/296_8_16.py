def find_pairs_with_ratio(start, end, target_ratio):
    pairs = []
    for i in range(start, end + 1):
        if i * target_ratio % 1 == 0:
            j = int(i * target_ratio)
            if start <= j <= end:
                pairs.append((i, j))
    return pairs

if __name__ == '__main__':
    sample_pairs = find_pairs_with_ratio(1, 100, 2/3)
    print(sample_pairs)