def equal_lists_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    whether two lists of equal length contain identical elements in order.
    
    Args:
        list1 (list): First list to compare.
        list2 (list): Second list to compare.
        
    Yields:
        bool: True if element-wise equal, False otherwise.
    """
    # Check lengths first
    if len(list1) != len(list2):
        yield False
        return

    for item in zip(list1, list2):
        if item[0] == item[1]:
            yield True
        else:
            yield False

if __name__ == '__main__':
    # Hard-coded sample values
    sample_list_a = [1, 2, 3, 'a', 4.5]
    sample_list_b = [1, 2, 3, 'b', 4.5]

    print("Comparing two lists:")
    results = list(equal_lists_generator(sample_list_a, sample_list_b))
    
    if all(results):
        print(f"Lists are equal: {sample_list_a} == {sample_list_b}")
    else:
        print(f"Lists differ at index 3 (values '{results[0]}' vs 'False')")

    # Additional test case with different lengths to ensure robustness check is present in generator logic
    sample_list_c = [1, 2, 3]
    sample_list_d = [1, 2]

    results_diff_len = list(equal_lists_generator(sample_list_c, sample_list_d))
    print(f"Different length test: {results_diff_len}")