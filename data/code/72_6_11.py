def compare_lists(list1, list2):
    comparison_map = {
        True: "{} == {}",
        False: "{} != {}"
    }
    return [comparison_map[x == y].format(x, y) for x, y in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [3, 7, 12, 18]
    sample_list2 = [3, 6, 15, 18]
    comparison_results = compare_lists(sample_list1, sample_list2)
    for result in comparison_results:
        print(result)