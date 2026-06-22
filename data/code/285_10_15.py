def max_adjacent_pairs(lst):
    results = []
    for i in range(len(lst) - 1):
        pair_max = max(lst[i], lst[i + 1])
        results.append(pair_max)
    return results

if __name__ == '__main__':
    sample_list = [4, 1, 7, 3, 2]
    print(max_adjacent_pairs(sample_list))