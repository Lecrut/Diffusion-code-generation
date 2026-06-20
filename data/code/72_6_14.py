def validate_lists(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length.")

def compare_elements(item1, item2):
    if item1 > item2:
        return f"{item1} > {item2}"
    elif item1 < item2:
        return f"{item1} < {item2}"
    else:
        return f"{item1} == {item2}"

def compare_lists(list1, list2):
    validate_lists(list1, list2)
    results = [compare_elements(item1, item2) for item1, item2 in zip(list1, list2)]
    return results

if __name__ == '__main__':
    sample_list1 = [1, 5, 10, 15]
    sample_list2 = [2, 4, 10, 20]
    comparison_results = compare_lists(sample_list1, sample_list2)
    for result in comparison_results:
        print(result)