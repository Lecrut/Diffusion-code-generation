def max_adjacent_pairs(lst):
    results = []
    for i in range(len(lst) - 1):
        a, b = lst[i], lst[i+1]
        results.append(max(a, b))
    return results

if __name__ == '__main__':
    sample_data = [4, 2, 9, 7, 5, 6]
    max_values = max_adjacent_pairs(sample_data)
    print(max_values)