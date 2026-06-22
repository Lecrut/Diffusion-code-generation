def compare_lists(list1, list2):
    comparison_results = []
    for value_first, value_second in zip(list1, list2):
        if value_first < value_second:
            relation = "less than"
        elif value_first > value_second:
            relation = "greater than"
        else:
            relation = "equal to"
        comparison_results.append((value_first, value_second, relation))
    return comparison_results

if __name__ == '__main__':
    sample_list_one = [10, 20, 30]
    sample_list_two = [10, 15, 35]
    result = compare_lists(sample_list_one, sample_list_two)
    print(result)