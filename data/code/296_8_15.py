def find_pairs_with_ratio(start, end, ratio):
    pairs = []
    for i in range(start, end + 1):
        if i % (ratio[0] / ratio[1]) == 0:
            j = int(i * ratio[1] / ratio[0])
            if start <= j <= end:
                pairs.append((i, j))
    return pairs

if __name__ == '__main__':
    result = find_pairs_with_ratio(1, 100, (2, 3))
    print(result)