def max_adjacent_pairs(lst):
    return [max(lst[i], lst[i+1]) for i in range(len(lst) - 1)]

if __name__ == '__main__':
    sample_list = [4, 1, 7, 3, 5]
    print(max_adjacent_pairs(sample_list))