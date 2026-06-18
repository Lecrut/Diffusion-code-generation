def swap_neighbors(lst):
    return [lst[i] if i % 2 == 0 else lst[i + 1] for i in range(0, len(lst) - 1, 2)]
if __name__ == '__main__':
    sample_list = [34, 56, 78, 90, 12, 34]
    swapped_result = swap_neighbors(sample_list.copy())
    print(swapped_result)