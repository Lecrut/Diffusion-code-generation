def compare_lists(list1, list2):
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers.")
    
    return [f"{item1} == {item2}" if item1 == item2 else f"{item1} {'>' if item1 > item2 else '<'} {item2}" for item1, item2 in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [1, 5, 10, 15]
    sample_list2 = [2, 4, 10, 20]
    comparison_results = compare_lists(sample_list1, sample_list2)
    for result in comparison_results:
        print(result)