def compare_lists(list1, list2):
    results = []
    for item1, item2 in zip(list1, list2):
        if item1 > item2:
            results.append(f"{item1} is greater than {item2}")
        elif item1 < item2:
            results.append(f"{item1} is less than {item2}")
        else:
            results.append(f"{item1} is equal to {item2}")
    return results

if __name__ == '__main__':
    sample_list_a = [1, 5, 10, 15]
    sample_list_b = [2, 4, 10, 20]
    comparison_results = compare_lists(sample_list_a, sample_list_b)
    for result in comparison_results:
        print(result)