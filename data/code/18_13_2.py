def is_first_greater_than_second(lst):
    """Check if the first element of the list is greater than the second."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3, 8]
    result = is_first_greater_than_second(sample_list)
    print(f"{sample_list}[0] ({sample_list[0]}) > {sample_list}[1] ({sample_list[1]}): {result}")

    # Additional test case where the condition is false
    sample_list_2 = [2, 4, 6]
    result_2 = is_first_greater_than_second(sample_list_2)
    print(f"{sample_list_2}[0] ({sample_list_2[0]}) > {sample_list_2}[1] ({sample_list_2[1]}): {result_2}")

    # Test case with negative numbers
    sample_list_3 = [-1, -5, 0]
    result_3 = is_first_greater_than_second(sample_list_3)
    print(f"{sample_list_3}[0] ({sample_list_3[0]}) > {sample_list_3}[1] ({sample_list_3[1]}): {result_3}")