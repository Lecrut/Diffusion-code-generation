def max_adjacent_pairs(lst):
    return [max(lst[i:i+2]) for i in range(len(lst) - 1)]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(max_adjacent_pairs(sample_list))