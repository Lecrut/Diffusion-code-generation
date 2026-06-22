def find_pairs_with_ratio(target_ratio, start, end):
    pairs = []
    for i in range(start, end + 1):
        if i * target_ratio == int(i * target_ratio) and start <= int(i * target_ratio) <= end:
            pairs.append((i, int(i * target_ratio)))
    return pairs

if __name__ == '__main__':
    print(find_pairs_with_ratio(2, 1, 10))