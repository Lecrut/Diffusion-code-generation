def max_adjacent_pairs(lst):
    return [max(lst[i:i+2]) for i in range(len(lst) - 1)]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1]
    print(max_adjacent_pairs(sample_list))