def max_adjacent_pairs(lst):
    return [max(a, b) for a, b in zip(lst, lst[1:])]

if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4]
    print(max_adjacent_pairs(sample_list))