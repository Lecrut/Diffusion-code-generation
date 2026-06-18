def swap_neighbors(lst):
    result = []
    for i in range(len(lst) - 1):
        yield lst[i], lst[i + 1]
    if len(lst) > 0:
        yield lst[-1]
if __name__ == '__main__':
    sample_list = [3, 6, 9, 12, 15]
    swapped_pairs = list(swap_neighbors(sample_list))
    print(swapped_pairs)