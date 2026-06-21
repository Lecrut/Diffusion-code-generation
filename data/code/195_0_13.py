def lists_are_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            return False
    return True

if __name__ == '__main__':
    sample_list_a = [1, 5, 3, 7, 9]
    sample_list_b = [1, 5, 4, 7, 9]
    result = lists_are_identical(sample_list_a, sample_list_b)
    print(f"List A: {sample_list_a}")
    print(f"List B: {sample_list_b}")
    print("Lists are identical:" if result else "Lists are not identical")