def compare_adjacent_elements(lst):
    results = []
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            results.append('increasing')
        elif lst[i] > lst[i + 1]:
            results.append('decreasing')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 7, 7]
    print(compare_adjacent_elements(sample_list))