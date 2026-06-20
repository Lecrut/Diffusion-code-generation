def find_inequality_indices(lst):
    results = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            results.append((i, lst[i], lst[i + 1]))
    return results

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_inequality_indices(sample_list))