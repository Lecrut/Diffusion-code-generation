def compare_adjacent_elements(lst):
    results = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            results.append((i, lst[i], lst[i + 1]))
    return results

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    output = compare_adjacent_elements(sample_list)
    print(output)