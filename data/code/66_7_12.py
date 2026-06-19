def compare_adjacent_ascending(lst):
    return [lst[i] < lst[i + 1] for i in range(len(lst) - 1)]

if __name__ == '__main__':
    sample_list = [1, 3, 2, 4, 5]
    result = compare_adjacent_ascending(sample_list)
    print(result)