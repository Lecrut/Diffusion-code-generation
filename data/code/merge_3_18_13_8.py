def check_first_greater_than_second(lst):
    """Check if the first element is greater than the second in a list."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3, 2, 4]
    result = check_first_greater_than_second(sample_list)
    print(f"First element ({sample_list[0]}) is greater than second element ({sample_list[1]}): {result}")

    # Test with a case where it's not true
    sample_list_false = [2, 5, 3, 4]
    result_false = check_first_greater_than_second(sample_list_false)
    print(f"First element ({sample_list_false[0]}) is greater than second element ({sample_list_false[1]}): {result_false}")