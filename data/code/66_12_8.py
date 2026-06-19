def compare_adjacent_pairs(lst):
    return [max(a, b) for a, b in zip(lst, lst[1:])]

if __name__ == '__main__':
    sample_list = [3, 6, 2, 8, 5, 9]
    result = compare_adjacent_pairs(sample_list)
    print(result)