def max_adjacent_pairs(lst):
    return [max(a, b) for a, b in zip(lst, lst[1:])]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1]
    print(max_adjacent_pairs(sample_list))