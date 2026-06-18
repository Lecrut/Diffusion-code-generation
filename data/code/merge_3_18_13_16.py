def is_first_greater_than_second(lst):
    """Check if the first element of a list is greater than the second."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    result = is_first_greater_than_second(sample_list)
    print(f"{sample_list} -> First element {sample_list[0]} is greater than second element {sample_list[1]}: {result}")

    # Additional test case where it's false
    sample_list_two = [2, 7]
    result_two = is_first_greater_than_second(sample_list_two)
    print(f"{sample_list_two} -> First element {sample_list_two[0]} is greater than second element {sample_list_two[1]}: {result_two}")