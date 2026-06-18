def check_first_greater_than_second(lst):
    """Check if the first element of a list is greater than the second."""
    return lst[0] > lst[1]

if __name__ == '__main__':
    test_list = [5, 3]
    result = check_first_greater_than_second(test_list)
    print(f"{test_list[0]} > {test_list[1]} is {result}")

    # Example with False case
    test_list_2 = [4, 6]
    result_2 = check_first_greater_than_second(test_list_2)
    print(f"{test_list_2[0]} > {test_list_2[1]} is {result_2}")