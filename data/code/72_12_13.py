def find_inequality_indices(lst):
    indices = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            indices.append((i, lst[i], lst[i + 1]))
    return indices

if __name__ == '__main__':
    sample_list = [1, 2, 3, 5, 5, 6, 7, 8, 9]
    print(find_inequality_indices(sample_list))