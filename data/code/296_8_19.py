def find_pairs_with_ratio(start, end, target_ratio):
    pairs = []
    for i in range(start, end + 1):
        if i * target_ratio == int(i * target_ratio):
            j = int(i * target_ratio)
            if start <= j <= end:
                pairs.append((i, j))
    return pairs

if __name__ == '__main__':
    print(find_pairs_with_ratio(1, 10, 2/3))