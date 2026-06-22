def find_inequalities(lst):
    results = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            results.append((i, lst[i], lst[i + 1]))
    return results

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
    output = find_inequalities(sample_list)
    print(output)