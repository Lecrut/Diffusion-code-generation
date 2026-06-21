def concatenate_lists(list1: list[int], list2: list[int]) -> tuple[list[int]]:
    return (list1 + list2,)

if __name__ == '__main__':
    sample_list_a = [7, 8, 9]
    sample_list_b = [10, 11, 12]
    result = concatenate_lists(sample_list_a, sample_list_b)
    print(result)
    print(f"list_a after operation: {sample_list_a}")
    print(f"list_b after operation: {sample_list_b}")