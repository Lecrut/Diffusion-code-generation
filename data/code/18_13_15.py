def check_first_greater_than_second(lst):
    """Directly evaluate if the first element is greater than the second in a list."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    result = check_first_greater_than_second(sample_list)
    print(f"{sample_list[0]} {'>'}{sample_list[1]}: {result}")

    test_case_two = ["a", "b"]
    # Assuming lexicographical order where 'a' < 'b', this should return False
    result2 = check_first_greater_than_second(test_case_two)
    print(f"'{test_case_two[0]}' '{'>'}'{test_case_two[1]}: {result2}")